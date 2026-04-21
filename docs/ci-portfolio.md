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

(List the custom signals you created and why.)

### Artifacts

(clickable link to artifacts/ folder and explain result files)

### Insights

(What did the signals reveal?)

## 4. Rolling Monitoring

### [Repository Link](https://github.com/ajaneh/cintel-04-rolling-monitoring)

### Techniques

(Explain how rolling windows were used.)

### Artifacts

(clickable link to artifacts/ folder and explain result files)

### Insights

(What patterns appeared?)

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
