# Continuous Intelligence Portfolio

Alex Heyert

2026-04

This page summarizes my work on **continuous intelligence** projects.

## 1. Professional Project

### [Repository Link](https://github.com/ajaneh/cintel-01-getting-started)

### Brief Overview of Project Tools and Choices

All data pipelines in these repositories were built with a consistent, high-performance tech stack to ensure reproducibility and rapid execution:

*   **Runtime:** `Python 3.14` (Leveraging the latest language features and performance optimizations)
*   **Tooling & Env Management:** `uv` (Used for lightning-fast dependency resolution and deterministic environments)
*   **Data Engine:** `Polars` (Utilized for multi-threaded, high-performance data manipulation and analysis)
*   **Visualization:** `Matplotlib` (Standardized framework for all analytical plotting and reporting)

## 2. Anomaly Detection

### [Repository Link](https://github.com/ajaneh/cintel-02-static-anomalies)

### Techniques

I used example data for an adult clinic that contained age and height. Anomalies were detected with rule based flagging. Initially the project used thresholds for age and height. My modification calculated the Z scores for age and height and used a threshold of ± 2. 

### Artifacts

[Artifacts Folder](https://github.com/ajaneh/cintel-02-static-anomalies/tree/main/artifacts)
![Scatterplot](https://github.com/ajaneh/cintel-02-static-anomalies/blob/main/artifacts/scatter_plot_alex.png)


### Insights

Use of Z score only flagged one anomaly, a patient 118 years old. This a notable outlier visible in the scatterplot. It's also interesting to note that as age increased height decreased, which is consistent with the real life phenomenon. 

## 3. Signal Design

### [Repository Link](https://github.com/ajaneh/cintel-03-signal-design)

### Signals

The signals used were Error rate (Errors ÷ Requests) and Average latency time (Latency ÷ Requests). Latency percentiles were calculated as well and tail latencies were logged. 

### Artifacts
![Histogram](https://github.com/ajaneh/cintel-03-signal-design/blob/main/artifacts/latency_histogram.png)

![SignalsVLatency](https://github.com/ajaneh/cintel-03-signal-design/blob/main/artifacts/requests_error_rate_vs_latency.png)
[Aritfacts Folder](https://github.com/ajaneh/cintel-03-signal-design/tree/main/artifacts)

### Insights

Only 3 of the data rows had a latency above the 90th percentile. Of these three the error rate was on the higher side, averaging around 4.5%, the total number of requests was also high.
Without detailed latency information (latency per request versus per error, for example) it's difficult to determine if errors are slow or if more requests result in greater latency. 

## 4. Rolling Monitoring

### [Repository Link](https://github.com/ajaneh/cintel-04-rolling-monitoring)

### Techniques

I acquired ridership data from the Chicago Transit Autority. I used their data portal to simplify the data I exported and used. After grouping by date I aggregated the sum of rows from the "rides" field, because I was interested in rides over time rather than rides per seperate station.

The rolling mean was the main signal of interest. The size of the window was adjusted several times in order to meaningfully smooth out noise. When choosing window size it's important to understand the natural time sequences of the data you're working with.

### Artifacts
![Monthly Window](https://github.com/ajaneh/cintel-04-rolling-monitoring/blob/main/artifacts/window_30.png) ![Annual Window](https://github.com/ajaneh/cintel-04-rolling-monitoring/blob/main/artifacts/window_365.png)


[Artifact Folder](https://github.com/ajaneh/cintel-04-rolling-monitoring/tree/main/artifacts)

### Insights

Noise reduced as window size increased. When looking at the graph with a "monthly window" it appears that ridership increased in warmer seasons (summer, fall) and sharply decreased in the winter and spring.
Ridership seems to increase from 2001 until it's maximum in 2015. We then see a dramatic decrease around 2019 - 2020. Since we know larger winows increase lag it's reasonable to assume that the dramatic decrease was caused by the COVID shutdowns. Ridership has increased in the last 5 years but not to pre 2020 averages. This may be indicicative of the increase in remote jobs since COVID.

## 5. Drift Detection

### [Repository Link](https://github.com/ajaneh/cintel-05-drift-detection)

### Techniques

(Explain how reference and current periods were compared.)

### Artifacts

(clickable link to artifacts/ folder and explain result files)

### Insights

(What changed? How do you know? How does this help make actionable decisions?)

## 6. Continuous Intelligence Pipeline

### [Repository Link](https://github.com/ajaneh/cintel-06-continuous-intelligence)

### Techniques

(Describe how signals and monitoring techniques were combined.)

### Artifacts

(clickable link to artifacts/ folder and explain result files)

### Assessment

(What does the pipeline say about the system state?)
