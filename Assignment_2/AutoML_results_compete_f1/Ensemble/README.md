# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                                    |   Weight |
|:-----------------------------------------|---------:|
| 28_LightGBM_KMeansFeatures_BoostOnErrors |        1 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.347268 |  nan        |
| auc       | 0.985774 |  nan        |
| f1        | 0.973799 |    0.503697 |
| accuracy  | 0.973799 |    0.503697 |
| precision | 0.993464 |    0.671509 |
| recall    | 1        |    0.051081 |
| mcc       | 0.947598 |    0.503697 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.347268 |  nan        |
| auc       | 0.985774 |  nan        |
| f1        | 0.973799 |    0.503697 |
| accuracy  | 0.973799 |    0.503697 |
| precision | 0.973799 |    0.503697 |
| recall    | 0.973799 |    0.503697 |
| mcc       | 0.947598 |    0.503697 |


## Confusion matrix (at threshold=0.503697)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              223 |                6 |
| Labeled as 1 |                6 |              223 |

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
