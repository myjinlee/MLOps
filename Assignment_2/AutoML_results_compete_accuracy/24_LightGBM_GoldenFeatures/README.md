# Summary of 24_LightGBM_GoldenFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 95
- **learning_rate**: 0.05
- **feature_fraction**: 1.0
- **bagging_fraction**: 1.0
- **min_data_in_leaf**: 10
- **metric**: custom
- **custom_eval_metric_name**: accuracy
- **explain_level**: 0

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
accuracy

## Training time

5.1 seconds

## Metric details
|           |   score |   threshold |
|:----------|--------:|------------:|
| logloss   | 0.10668 | nan         |
| auc       | 1       | nan         |
| f1        | 1       |   0.362868  |
| accuracy  | 1       |   0.362868  |
| precision | 1       |   0.362868  |
| recall    | 1       |   0.0306596 |
| mcc       | 1       |   0.362868  |


## Metric details with threshold from accuracy metric
|           |   score |   threshold |
|:----------|--------:|------------:|
| logloss   | 0.10668 |  nan        |
| auc       | 1       |  nan        |
| f1        | 1       |    0.362868 |
| accuracy  | 1       |    0.362868 |
| precision | 1       |    0.362868 |
| recall    | 1       |    0.362868 |
| mcc       | 1       |    0.362868 |


## Confusion matrix (at threshold=0.362868)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               23 |                0 |
| Labeled as 1 |                0 |               23 |

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
