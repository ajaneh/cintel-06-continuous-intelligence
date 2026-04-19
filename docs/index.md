# Continuous Intelligence

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## Custom Project

### Dataset
I used the provided dataset system_metrics which contains number of requests, number of errors, and latency time (ms).

### Signals
The signals of interest that were created were averages and z scores for Error rate and Latency.
The system was summarized with the averages of each incoming signal. Then expanded to include average error rate, average latency, and average Z scores for error rate and latency.

![Raw Data]((/artifacts/raw_metrics.png))

For the plot the signals were smoothed by a rolling average with a window of 5
![Signals](/artifacts/signals.png)

### Experiments
I began by plotting the raw data and the signals after creation. I experimented with adding more signals such as rolling averages and rolling standard deviation. Ultimately I did not use rolling signals to adjust system state summary. It didn't seem relevant to determining the overall system status. I added the field degradation reason to the system summary.

### Results
The averages of this small dataset do indicate stability,both calculated z scores were less than 0.3. I added detected anomalies to the log.

### Interpretation
I think a small dataset doesn't allow much room for meaningful interpretation. However if I think of this as one part of a larger dataset, perhaps representative of metrics every 5 minutes, this system summary would be useful for detecting system abnormalities.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Glossary** - project terms and concepts

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
