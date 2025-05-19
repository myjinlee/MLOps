# Summary of 121_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 40
- **max_depth**: 7
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

23.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.229052 |  nan        |
| auc       | 0.976211 |  nan        |
| f1        | 0.924779 |    0.535734 |
| accuracy  | 0.927948 |    0.643181 |
| precision | 1        |    0.735817 |
| recall    | 1        |    0        |
| mcc       | 0.862842 |    0.643181 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.229052 |  nan        |
| auc       | 0.976211 |  nan        |
| f1        | 0.923077 |    0.643181 |
| accuracy  | 0.927948 |    0.643181 |
| precision | 0.99     |    0.643181 |
| recall    | 0.864629 |    0.643181 |
| mcc       | 0.862842 |    0.643181 |


## Confusion matrix (at threshold=0.643181)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              227 |                2 |
| Labeled as 1 |               31 |              198 |

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
