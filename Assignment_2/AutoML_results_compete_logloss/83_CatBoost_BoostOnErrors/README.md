# Summary of 83_CatBoost_BoostOnErrors

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 7
- **rsm**: 0.7
- **loss_function**: Logloss
- **eval_metric**: Logloss
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

44.0 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0933352 | nan           |
| auc       | 0.995061  | nan           |
| f1        | 0.969697  |   0.171493    |
| accuracy  | 0.969432  |   0.171493    |
| precision | 1         |   0.954979    |
| recall    | 1         |   0.000102049 |
| mcc       | 0.939008  |   0.171493    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0933352 |  nan        |
| auc       | 0.995061  |  nan        |
| f1        | 0.969697  |    0.171493 |
| accuracy  | 0.969432  |    0.171493 |
| precision | 0.961373  |    0.171493 |
| recall    | 0.978166  |    0.171493 |
| mcc       | 0.939008  |    0.171493 |


## Confusion matrix (at threshold=0.171493)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              220 |                9 |
| Labeled as 1 |                5 |              224 |

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
