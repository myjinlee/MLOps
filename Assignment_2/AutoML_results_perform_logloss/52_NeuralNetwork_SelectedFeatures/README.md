# Summary of 52_NeuralNetwork_SelectedFeatures

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

10.0 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.206625 | nan          |
| auc       | 0.974428 | nan          |
| f1        | 0.946667 |   0.506958   |
| accuracy  | 0.947598 |   0.506958   |
| precision | 1        |   0.986886   |
| recall    | 1        |   1.2314e-07 |
| mcc       | 0.895743 |   0.506958   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.206625 |  nan        |
| auc       | 0.974428 |  nan        |
| f1        | 0.946667 |    0.506958 |
| accuracy  | 0.947598 |    0.506958 |
| precision | 0.963801 |    0.506958 |
| recall    | 0.930131 |    0.506958 |
| mcc       | 0.895743 |    0.506958 |


## Confusion matrix (at threshold=0.506958)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              221 |                8 |
| Labeled as 1 |               16 |              213 |

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
