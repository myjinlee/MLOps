# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

7.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.31362  | nan         |
| auc       | 0.924682 | nan         |
| f1        | 0.877193 |   0.393939  |
| accuracy  | 0.878261 |   0.393939  |
| precision | 1        |   0.85      |
| recall    | 1        |   0.0782609 |
| mcc       | 0.757035 |   0.393939  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.31362  |  nan        |
| auc       | 0.924682 |  nan        |
| f1        | 0.877193 |    0.393939 |
| accuracy  | 0.878261 |    0.393939 |
| precision | 0.892857 |    0.393939 |
| recall    | 0.862069 |    0.393939 |
| mcc       | 0.757035 |    0.393939 |


## Confusion matrix (at threshold=0.393939)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               51 |                6 |
| Labeled as 1 |                8 |               50 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
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
