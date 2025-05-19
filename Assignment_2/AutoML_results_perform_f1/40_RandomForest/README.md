# Summary of 40_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 40
- **max_depth**: 7
- **eval_metric_name**: f1
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
f1

## Training time

24.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.302278 |  nan        |
| auc       | 0.969699 |  nan        |
| f1        | 0.916844 |    0.5789   |
| accuracy  | 0.917031 |    0.614978 |
| precision | 1        |    0.700223 |
| recall    | 0.995633 |    0        |
| mcc       | 0.834093 |    0.614978 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.302278 |  nan        |
| auc       | 0.969699 |  nan        |
| f1        | 0.916667 |    0.614978 |
| accuracy  | 0.917031 |    0.614978 |
| precision | 0.920705 |    0.614978 |
| recall    | 0.912664 |    0.614978 |
| mcc       | 0.834093 |    0.614978 |


## Confusion matrix (at threshold=0.614978)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              211 |               18 |
| Labeled as 1 |               20 |              209 |

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
