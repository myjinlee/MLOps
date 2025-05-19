# Summary of 99_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: entropy
- **max_depth**: 3
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
f1

## Training time

14.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.297782 | nan         |
| auc       | 0.934641 | nan         |
| f1        | 0.868369 |   0.0479452 |
| accuracy  | 0.864629 |   0.482759  |
| precision | 1        |   0.875     |
| recall    | 1        |   0.0302013 |
| mcc       | 0.729703 |   0.482759  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.297782 |  nan        |
| auc       | 0.934641 |  nan        |
| f1        | 0.866953 |    0.482759 |
| accuracy  | 0.864629 |    0.482759 |
| precision | 0.852321 |    0.482759 |
| recall    | 0.882096 |    0.482759 |
| mcc       | 0.729703 |    0.482759 |


## Confusion matrix (at threshold=0.482759)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              194 |               35 |
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
