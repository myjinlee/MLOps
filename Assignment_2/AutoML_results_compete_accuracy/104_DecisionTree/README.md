# Summary of 104_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: entropy
- **max_depth**: 3
- **explain_level**: 0

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
accuracy

## Training time

3.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.277082 | nan         |
| auc       | 0.946125 | nan         |
| f1        | 0.913043 |   0.454545  |
| accuracy  | 0.913043 |   0.454545  |
| precision | 1        |   0.861111  |
| recall    | 1        |   0.0384146 |
| mcc       | 0.826087 |   0.454545  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.277082 |  nan        |
| auc       | 0.946125 |  nan        |
| f1        | 0.913043 |    0.454545 |
| accuracy  | 0.913043 |    0.454545 |
| precision | 0.913043 |    0.454545 |
| recall    | 0.913043 |    0.454545 |
| mcc       | 0.826087 |    0.454545 |


## Confusion matrix (at threshold=0.454545)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               21 |                2 |
| Labeled as 1 |                2 |               21 |

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
