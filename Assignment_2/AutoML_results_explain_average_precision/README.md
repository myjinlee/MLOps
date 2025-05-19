# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type       |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:------------------|---------------:|-------------:|
|              | [1_Baseline](1_Baseline/README.md)                           | Baseline       | average_precision |       0.504348 |         1.57 |
|              | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | average_precision |       0.9227   |         3.02 |
|              | [3_Linear](3_Linear/README.md)                               | Linear         | average_precision |       0.986073 |         3.88 |
| **the best** | [4_Default_Xgboost](4_Default_Xgboost/README.md)             | Xgboost        | average_precision |       1        |         4.43 |
|              | [5_Default_NeuralNetwork](5_Default_NeuralNetwork/README.md) | Neural Network | average_precision |       0.992316 |         2.77 |
|              | [6_Default_RandomForest](6_Default_RandomForest/README.md)   | Random Forest  | average_precision |       0.986895 |         3.49 |
|              | [Ensemble](Ensemble/README.md)                               | Ensemble       | average_precision |       1        |         1.56 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

