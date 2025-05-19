# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                      |   Weight |
|:---------------------------|---------:|
| 101_CatBoost               |        1 |
| 101_CatBoost_BoostOnErrors |        1 |
| 104_CatBoost               |        1 |
| 15_Xgboost                 |       72 |
| 16_Xgboost                 |       18 |
| 19_Xgboost                 |       22 |
| 24_LightGBM                |        1 |
| 32_CatBoost                |        1 |
| 33_CatBoost_GoldenFeatures |        1 |
| 72_NearestNeighbors        |        2 |
| 74_CatBoost                |        1 |
| 76_CatBoost                |        3 |
| 91_NeuralNetwork           |        2 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.615328 |  nan        |
| auc       | 0.994718 |  nan        |
| f1        | 0.969432 |    0.492953 |
| accuracy  | 0.969432 |    0.492953 |
| precision | 1        |    0.540729 |
| recall    | 1        |    0.406367 |
| mcc       | 0.938865 |    0.492953 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.615328 |  nan        |
| auc       | 0.994718 |  nan        |
| f1        | 0.969432 |    0.492953 |
| accuracy  | 0.969432 |    0.492953 |
| precision | 0.969432 |    0.492953 |
| recall    | 0.969432 |    0.492953 |
| mcc       | 0.938865 |    0.492953 |


## Confusion matrix (at threshold=0.492953)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              222 |                7 |
| Labeled as 1 |                7 |              222 |

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
