# Summary of 3_Linear

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

6.3 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.163214 | nan          |
| auc       | 0.980944 | nan          |
| f1        | 0.948276 |   0.41277    |
| accuracy  | 0.947826 |   0.41277    |
| precision | 1        |   0.568079   |
| recall    | 1        |   0.00812168 |
| mcc       | 0.900647 |   0.568079   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.163214 |   nan       |
| auc       | 0.980944 |   nan       |
| f1        | 0.948276 |     0.41277 |
| accuracy  | 0.947826 |     0.41277 |
| precision | 0.948276 |     0.41277 |
| recall    | 0.948276 |     0.41277 |
| mcc       | 0.895644 |     0.41277 |


## Confusion matrix (at threshold=0.41277)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               54 |                3 |
| Labeled as 1 |                3 |               55 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature               |   Learner_1 |
|:----------------------|------------:|
| PEER_PRESSURE         |   1.90678   |
| YELLOW_FINGERS        |   1.73776   |
| CHRONIC DISEASE       |   1.69633   |
| ALLERGY               |   1.68397   |
| SWALLOWING DIFFICULTY |   1.65569   |
| COUGHING              |   1.60986   |
| ALCOHOL CONSUMING     |   1.59961   |
| FATIGUE               |   1.27991   |
| WHEEZING              |   1.19506   |
| ANXIETY               |   0.865616  |
| SMOKING               |   0.36864   |
| CHEST PAIN            |   0.244263  |
| SHORTNESS OF BREATH   |   0.108942  |
| AGE                   |   0.10044   |
| GENDER                |  -0.0231852 |
| intercept             |  -4.98493   |


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



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions for class 0 (Fold 1)
![SHAP worst decisions class 0 from Fold 1](learner_fold_0_shap_class_0_worst_decisions.png)
### Top-10 Best decisions for class 0 (Fold 1)
![SHAP best decisions class 0 from Fold 1](learner_fold_0_shap_class_0_best_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 1)
![SHAP worst decisions class 1 from Fold 1](learner_fold_0_shap_class_1_worst_decisions.png)
### Top-10 Best decisions for class 1 (Fold 1)
![SHAP best decisions class 1 from Fold 1](learner_fold_0_shap_class_1_best_decisions.png)

[<< Go back](../README.md)
