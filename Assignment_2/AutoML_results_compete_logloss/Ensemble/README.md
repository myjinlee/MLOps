# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                     |   Weight |
|:--------------------------|---------:|
| 72_NearestNeighbors       |        3 |
| 75_CatBoost               |        8 |
| 76_CatBoost               |        9 |
| 83_CatBoost               |       19 |
| 83_CatBoost_BoostOnErrors |        3 |

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0914001 | nan           |
| auc       | 0.995748  | nan           |
| f1        | 0.965665  |   0.12503     |
| accuracy  | 0.965066  |   0.12503     |
| precision | 1         |   0.935736    |
| recall    | 1         |   7.52959e-05 |
| mcc       | 0.930699  |   0.12503     |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0914001 |   nan       |
| auc       | 0.995748  |   nan       |
| f1        | 0.965665  |     0.12503 |
| accuracy  | 0.965066  |     0.12503 |
| precision | 0.949367  |     0.12503 |
| recall    | 0.982533  |     0.12503 |
| mcc       | 0.930699  |     0.12503 |


## Confusion matrix (at threshold=0.12503)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              217 |               12 |
| Labeled as 1 |                4 |              225 |

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
