# Summary of 71_NearestNeighbors

[<< Go back](../README.md)


## k-Nearest Neighbors (Nearest Neighbors)
- **n_jobs**: -1
- **n_neighbors**: 7
- **weights**: uniform
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
f1

## Training time

8.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.512108 |  nan        |
| auc       | 0.961061 |  nan        |
| f1        | 0.911964 |    0.285714 |
| accuracy  | 0.914847 |    0.285714 |
| precision | 0.977612 |    0.857143 |
| recall    | 0.969432 |    0        |
| mcc       | 0.83148  |    0.285714 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.512108 |  nan        |
| auc       | 0.961061 |  nan        |
| f1        | 0.911964 |    0.285714 |
| accuracy  | 0.914847 |    0.285714 |
| precision | 0.943925 |    0.285714 |
| recall    | 0.882096 |    0.285714 |
| mcc       | 0.83148  |    0.285714 |


## Confusion matrix (at threshold=0.285714)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              217 |               12 |
| Labeled as 1 |               27 |              202 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
