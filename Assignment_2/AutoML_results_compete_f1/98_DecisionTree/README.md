# Summary of 98_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: entropy
- **max_depth**: 4
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
f1

## Training time

14.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.349729 |  nan        |
| auc       | 0.949658 |  nan        |
| f1        | 0.905579 |    0.415584 |
| accuracy  | 0.90393  |    0.415584 |
| precision | 0.994286 |    0.818182 |
| recall    | 0.9869   |    0        |
| mcc       | 0.808354 |    0.415584 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.349729 |  nan        |
| auc       | 0.949658 |  nan        |
| f1        | 0.905579 |    0.415584 |
| accuracy  | 0.90393  |    0.415584 |
| precision | 0.890295 |    0.415584 |
| recall    | 0.921397 |    0.415584 |
| mcc       | 0.808354 |    0.415584 |


## Confusion matrix (at threshold=0.415584)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              203 |               26 |
| Labeled as 1 |               18 |              211 |

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
