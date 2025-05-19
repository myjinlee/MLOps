# Summary of 10_Default_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
- **max_depth**: 4
- **eval_metric_name**: auc
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
auc

## Training time

5.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.2211   | nan         |
| auc       | 0.971015 | nan         |
| f1        | 0.91974  |   0.476987  |
| accuracy  | 0.919214 |   0.476987  |
| precision | 1        |   0.706181  |
| recall    | 1        |   0.0156714 |
| mcc       | 0.8385   |   0.476987  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.2211   |  nan        |
| auc       | 0.971015 |  nan        |
| f1        | 0.91974  |    0.476987 |
| accuracy  | 0.919214 |    0.476987 |
| precision | 0.913793 |    0.476987 |
| recall    | 0.925764 |    0.476987 |
| mcc       | 0.8385   |    0.476987 |


## Confusion matrix (at threshold=0.476987)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              209 |               20 |
| Labeled as 1 |               17 |              212 |

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
