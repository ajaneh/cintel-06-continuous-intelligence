# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

import matplotlib.pyplot as plt
import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P6", level="DEBUG")

# === DEFINE GLOBAL PATHS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "system_metrics_case.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "system_assessment_alex.csv"

# === DEFINE THRESHOLDS ===

# Analysts need to know their data and
# choose thresholds that make sense for their specific use case.

MAX_ERROR_RATE: Final[float] = 0.05
MAX_AVG_LATENCY: Final[float] = 36.0
MAX_ZSCORE: Final[float] = 2.0


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    # Ensure artifacts directory exists
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # ----------------------------------------------------
    # STEP 1: READ SYSTEM METRICS
    # ----------------------------------------------------
    df = pl.read_csv(DATA_FILE)

    LOG.info(f"STEP 1. Loaded {df.height} system records")

    # GRAPH RAW DATA
    # LOG.info("STEP 1. Graphing raw metrics...")
    fig1, ax1 = plt.subplots(1, 3, tight_layout=True)
    for col_name in df.columns:
        ax1[df.columns.index(col_name)].plot(df[col_name], marker='o')
        ax1[df.columns.index(col_name)].set_title(col_name)
    fig1.suptitle("Raw System Metrics")
    fig1.supylabel("Metric Value")
    fig1.supxlabel("Count")
    fig1.suptitle("Raw System Metrics")
    plt.savefig(ARTIFACTS_DIR / "raw_metrics.png")
    plt.close(fig1)
    # ----------------------------------------------------
    # STEP 2: DESIGN SIGNALS
    # ----------------------------------------------------
    # This step connects to Module 3: Signal Design.
    # Create useful signals derived from raw system metrics.

    LOG.info("STEP 2. Designing signals from raw metrics...")

    df = df.with_columns(
        [
            (pl.col("errors") / pl.col("requests")).alias("error_rate"),
            (pl.col("total_latency_ms") / pl.col("requests")).alias("avg_latency_ms"),
        ]
    )
    # Add rolling mean for z-score, zscore, rolling mean and rolling std for error_rate and avg_latency_ms
    df = df.with_columns(
        [
            pl.col("error_rate").rolling_std(5).alias("error_rate_roll_std"),
            pl.col("avg_latency_ms").rolling_std(5).alias("latency_roll_std"),
            pl.col("error_rate").rolling_mean(5).alias("error_rate_roll_mean"),
            pl.col("avg_latency_ms").rolling_mean(5).alias("latency_roll_mean"),
        ]
    )
    df = df.with_columns(
        [
            (
                (pl.col("error_rate") - pl.col("error_rate_roll_mean"))
                / pl.col("error_rate_roll_std")
            ).alias("error_rate_zscore"),
            (
                (pl.col("avg_latency_ms") - pl.col("latency_roll_mean"))
                / pl.col("latency_roll_std")
            ).alias("latency_zscore"),
        ]
    )

    # plot the signals
    fig2, ax2 = plt.subplots(1, 3, tight_layout=True)
    ax2[0].plot(df["error_rate_roll_mean"], marker='o')
    ax2[0].set_title("Rolling Error Rate")
    ax2[1].plot(df["latency_roll_mean"], marker='o')
    ax2[1].set_title("Rolling Average Latency (ms)")
    ax2[1].set_ylabel("Latency (ms)")
    ax2[2].plot(df["latency_roll_std"], marker='o')
    ax2[2].set_title("Latency Volatility (Rolling Std)")
    ax2[2].set_ylabel("Latency (ms)")
    fig2.suptitle("Derived System Signals")
    fig2.supxlabel("Count")
    plt.savefig(ARTIFACTS_DIR / "signals.png")
    plt.close(fig2)

    LOG.info("STEP 2. Signals designed and graphed")

    # ----------------------------------------------------
    # STEP 3: DETECT ANOMALIES
    # ----------------------------------------------------
    # This step connects to Module 2: Anomaly Detection.
    # Check whether signal values exceed reasonable thresholds.

    LOG.info("STEP 3. Checking for anomalies in system signals...")

    anomalies_df = df.filter(
        (pl.col("error_rate") > MAX_ERROR_RATE)
        | (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
        | (pl.col("error_rate_zscore") > MAX_ZSCORE)
        | (pl.col("latency_zscore") > MAX_ZSCORE)
    )
    LOG.info(
        f"STEP 3. Using thresholds: MAX_ERROR_RATE={MAX_ERROR_RATE}, "
        f"MAX_AVG_LATENCY={MAX_AVG_LATENCY}"
        f", Z-SCORE_THRESHOLD={MAX_ZSCORE}"
    )

    LOG.info(f"STEP 3. Anomalies detected: {anomalies_df}")

    # ----------------------------------------------------
    # STEP 4: SUMMARIZE CURRENT SYSTEM STATE
    # ----------------------------------------------------
    # This step brings together ideas from earlier modules:
    # - Module 3: Signal Design
    # - Module 2: Anomaly Detection
    # It then adds the main goal of Module 6:
    # assess the overall state of the system.

    # NOTE: recipes for column creation and filtering
    # can be done in place as we add signals and logic to a DataFrame.
    # When logic is more complex, it can be helpful to
    # break it into multiple steps/recipes
    # for readability and debugging as shown previously.

    LOG.info("STEP 4. Summarizing system state from monitored signals...")

    summary_df = df.select(
        [
            pl.col("requests").mean().round(3).alias("avg_requests"),
            pl.col("errors").mean().round(3).alias("avg_errors"),
            pl.col("error_rate").mean().round(3).alias("avg_error_rate"),
            pl.col("avg_latency_ms").mean().round(3).alias("avg_latency_ms"),
            pl.col("error_rate_zscore").mean().round(3).alias("avg_error_rate_zscore"),
            pl.col("latency_zscore").mean().round(3).alias("avg_latency_zscore"),
        ]
    )

    # Add a simple assessment label
    summary_df = summary_df.with_columns(
        pl.when(
            (pl.col("avg_error_rate") > MAX_ERROR_RATE)
            | (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
            | (pl.col("avg_error_rate_zscore").abs() > MAX_ZSCORE)
            | (pl.col("avg_latency_zscore").abs() > MAX_ZSCORE)
        )
        .then(pl.lit("DEGRADED"))
        .otherwise(pl.lit("STABLE"))
        .alias("system_state")
    )

    # Add a degradation reason
    summary_df = summary_df.with_columns(
        pl.when(
            (pl.col("avg_error_rate") > MAX_ERROR_RATE)
            & (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
        )
        .then(pl.lit("ERROR_RATE+LATENCY"))
        .when(pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
        .then(pl.lit("LATENCY"))
        .when(pl.col("avg_error_rate") > MAX_ERROR_RATE)
        .then(pl.lit("ERROR_RATE"))
        .otherwise(pl.lit("NONE"))
        .alias("degradation_reason"),
    )

    LOG.info(f"STEP 4. System summary:\n{summary_df}")
    LOG.info("STEP 4. System assessment completed")

    # ----------------------------------------------------
    # STEP 5: SAVE SYSTEM ASSESSMENT
    # ----------------------------------------------------
    summary_df.write_csv(OUTPUT_FILE)

    LOG.info(f"STEP 5. Wrote system assessment file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
