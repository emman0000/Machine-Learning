# Decision Tree Assignment

## Overview
This assignment involves building and evaluating Decision Tree models on two datasets from the UCI Machine Learning Repository. The datasets must have at least 10 attributes.

## Tasks

### 1. Model Training and Evaluation
Train Decision Tree models using the following criteria and report the accuracy scores:

| Model Type                    | Dataset1 Training Accuracy | Dataset1 Testing Accuracy | Dataset2 Training Accuracy | Dataset2 Testing Accuracy |
|-------------------------------|----------------------------|---------------------------|----------------------------|---------------------------|
| DT using gini (without pruning) |                            |                           |                            |                           |
| DT using gini (with pruning)    |                            |                           |                            |                           |
| DT using entropy (without pruning) |                         |                           |                            |                           |
| DT using entropy (with pruning)  |                         |                           |                            |                           |

**Hint:** Use `ccp_alpha = 0.015` for pruning.

---

### 2. Performance Summary for Dataset2 (Entropy with Pruning)
Combine the actual vs. predicted outputs for the testing data and summarize the performance as:






---

### 3. Model Fit Analysis
Plot training and testing accuracy graphs for both datasets across all four methods (8 graphs total). Use the graphs to analyze whether the models are:

- **Overfit**
- **Underfit**
- **Generalized**

---

## Dataset Source
- UCI ML Repository: [https://archive.ics.uci.edu/ml/datasets.php](https://archive.ics.uci.edu/ml/datasets.php)


