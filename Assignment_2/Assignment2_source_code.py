#!/usr/bin/env python
# coding: utf-8

# ## Libraries

# In[129]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Sklearn
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, GridSearchCV
# Models (some libraries are used to model selection process)
"""
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBRegressor, XGBClassifier
from lightgbm import LGBMRegressor, LGBMClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
"""


# In[130]:


np.random.seed(42)
random.seed(42)


# ##Load dataset

# In[131]:


# read csv file
df = pd.read_csv(f"./survey_lung_cancer.csv")
print(df)


# In[132]:


df.head()


# ##missing value check

# In[133]:


# check the number of missing values for each column
missing_values = df.isnull().sum()

# ouput only columns with missing values
missing_values = missing_values[missing_values > 0]

print(missing_values)
# Check that there are no missing values ​​in the print result


# In[134]:


df.info()


# ##Data distribution

# In[135]:


# numerical variable
numerical = ['AGE']

# categorical variable
categorical = [
    'GENDER', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE',
    'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
    'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
    'SWALLOWING DIFFICULTY', 'CHEST PAIN'
]
target = 'LUNG_CANCER'


# In[136]:


#look at numerical data distribution
for i in df[numerical].columns:
    plt.hist(df[numerical][i])
    plt.xticks()
    plt.xlabel(i)
    plt.ylabel('number of people')
    plt.show()


# In[137]:


#look at categorical data distribution except target
for idx, i in enumerate(df[categorical].columns):
    value_counts = df[categorical][i].value_counts()
    sns.barplot(x=value_counts.index, y=value_counts.values, palette=sns.color_palette("Set2", n_colors=len(value_counts)))
    plt.xlabel(i)
    plt.ylabel('number of people')
    plt.show()


# In[138]:


# target class distribution
value_counts_target = df[target].value_counts()
sns.barplot(x=value_counts_target.index, y=value_counts_target.values, palette=sns.color_palette("Set2", n_colors=len(value_counts_target)))
plt.xlabel(target)


# ## Transform the values

# - GENDER : M / F or M / W => 0 / 1
# - LUNG_CANCER :	YES / NO => 1 / 0
# - Other binary variables	YES / NO => 1 / 0

# In[139]:


# change the type of the valued ; string -> int not label encoding
#df.columns = [col.strip() for col in df.columns]  # remove empty space

# except fot AGE, GENDER, LUNG_CANCER columns, dealing with the rest columns
binary_cols = [col for col in df.columns if col not in ['AGE', 'GENDER', 'LUNG_CANCER']]

# transform the values ; 1(=NO), 2(=YES) -> 0(=NO), 1(=YES)
for col in binary_cols:
    df[col] = df[col].map({1: 0, 2: 1, '1': 0, '2': 1})  # also consider the case of containing string..

# GENDER: M → 0, W → 1
df['GENDER'] = df['GENDER'].astype(str).str.upper().map({'M': 0, 'F': 1})

# LUNG_CANCER: NO → 0, YES → 1
df['LUNG_CANCER'] = df['LUNG_CANCER'].astype(str).str.upper().map({'NO': 0, 'YES': 1})


# In[140]:


print(df)
df.info()


# ## Split the dataset for train and test

# In[141]:


# divide into properties(X) and target(y)
X = df.drop(columns=['LUNG_CANCER'])
y = df['LUNG_CANCER']

# Split Train/Test (85% train, 15% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42, stratify=y
)
# stratify=y ; Divide y by maintaining the class ratio on both train and test.


# In[142]:


# 결과 확인
print("Train shape:", X_train.shape, y_train.shape)
print("Test shape:", X_test.shape, y_test.shape)
print("Train label distribution:\n", y_train.value_counts(normalize=True))
print("Test label distribution:\n", y_test.value_counts(normalize=True))


# In[143]:


print(X.columns)


# ## Training & evaluation
# - Before training and after feature selection, perform SMOTE
# - Optimization by tuning model parameters
# - Since it is a binary classification problem, the classifier model is considered.

# In[144]:


random_state = 42
kf = KFold(n_splits=10, shuffle=True, random_state=random_state)
scoring = "recall"

models = {}


# In[145]:


from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTENC
from supervised.automl import AutoML
from catboost import CatBoostClassifier
from sklearn.metrics import (accuracy_score, f1_score, roc_auc_score,
                             precision_score, recall_score,
                             precision_recall_curve, auc,
                             balanced_accuracy_score, matthews_corrcoef)
from collections import Counter

# categorical feature 인덱스
categorical_indices = [i for i, col in enumerate(X_train.columns) if col!='AGE']
random_state = 42

# SMOTENC 적용 후 AutoML 적용
smote = SMOTENC(categorical_features=categorical_indices, random_state=42, k_neighbors=1)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)


# In[146]:


from supervised.automl import AutoML
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score, average_precision_score
import pandas as pd

# 사용할 평가 지표 목록
metrics_explain = ["logloss", "f1", "auc", "accuracy", "average_precision"]

# 학습된 모델, 예측 결과, 성능 저장용 dict
automl_models_explain = {}
predictions_explain = {}
test_scores_explain = {}

for metric in metrics_explain:
    print(f"\n▶ Training AutoML (Explain) with eval_metric = '{metric}'")

    # AutoML 실행
    automl_explain = AutoML(
        mode="Explain", 
        total_time_limit=1000,
        results_path=f"AutoML_results_explain_{metric}",
        eval_metric=metric
    )
    automl_explain.fit(X_resampled, y_resampled)
    
    # 리포트 생성 - README.html
    automl_explain.report()

    # 모델 및 예측 저장
    automl_models_explain[metric] = automl_explain
    preds = automl_explain.predict(X_test)
    predictions_explain[metric] = preds

    # 실제 test 성능 평가
    try:
        auc_score = roc_auc_score(y_test, preds)
    except:
        auc_score = "N/A"

    try:
        ap_score = average_precision_score(y_test, preds)
    except:
        ap_score = "N/A"

    test_scores_explain[metric] = {
        "Accuracy": accuracy_score(y_test, preds),
        "F1 Score": f1_score(y_test, preds),
        "Precision": precision_score(y_test, preds),
        "Recall": recall_score(y_test, preds),
        "ROC AUC": auc_score,
        "Average Precision": ap_score
    }

# 결과 테이블 출력
df_explain_results = pd.DataFrame(test_scores_explain).T
print("\n Test Set Evaluation Results (Explain mode):")
display(df_explain_results)


# In[147]:


from supervised.automl import AutoML
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score, average_precision_score
import pandas as pd

# 사용할 평가 지표 목록
metrics_compete = ["logloss", "f1", "auc", "accuracy", "average_precision"]

# 학습된 모델과 예측 결과 저장용 dict
automl_models_compete = {}
predictions_compete = {}
test_scores_compete = {}

for metric in metrics_compete:
    print(f"\n▶ Training AutoML (Compete) with eval_metric = '{metric}'")
    
    # AutoML 실행
    automl_compete = AutoML(
        mode="Compete",
        total_time_limit=2000,
        results_path=f"AutoML_results_compete_{metric}",
        eval_metric=metric
    )
    automl_compete.fit(X_resampled, y_resampled)
    
    # 리포트 생성 - README.html
    automl_compete.report()

    # 모델 및 예측 저장
    automl_models_compete[metric] = automl_compete
    preds_compete = automl_compete.predict(X_test)
    predictions_compete[metric] = preds_compete

    # 실제 test 성능 평가
    try:
        auc_score = roc_auc_score(y_test, preds_compete)
    except:
        auc_score = "N/A"

    try:
        ap_score = average_precision_score(y_test, preds_compete)
    except:
        ap_score = "N/A"

    test_scores_compete[metric] = {
        "Accuracy": accuracy_score(y_test, preds_compete),
        "F1 Score": f1_score(y_test, preds_compete),
        "Precision": precision_score(y_test, preds_compete),
        "Recall": recall_score(y_test, preds_compete),
        "ROC AUC": auc_score,
        "Average Precision": ap_score
    }

# 결과 테이블 출력
df_compete_results = pd.DataFrame(test_scores_compete).T
print("\n Test Set Evaluation Results (by metric):")
display(df_compete_results)


# ## Artifacts analysis

# In[148]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ### Explain mode

# In[149]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os
import glob

# 여러 metric 실험 결과가 저장된 폴더들 지정 (예시)
results_folders = [
    "AutoML_results_explain_logloss",
    "AutoML_results_explain_f1",
    "AutoML_results_explain_auc",
    "AutoML_results_explain_accuracy",
    "AutoML_results_explain_precision",
    "AutoML_results_explain_recall"
]

for results_path in results_folders:
    if not os.path.exists(os.path.join(results_path, "leaderboard.csv")):
        print(f"[ X ] {results_path} → leaderboard.csv 없음. 건너뜁니다.")
        continue

    print(f"\n Analyzing results in: {results_path}\n")

    # 1. 리더보드 불러오기
    leaderboard = pd.read_csv(os.path.join(results_path, "leaderboard.csv"))

    # 2. metric_type 종류 확인 및 피벗
    metric_types = leaderboard["metric_type"].unique()
    pivot = leaderboard.pivot_table(index=["name", "model_type"], 
                                     columns="metric_type", 
                                     values="metric_value")
    print("Metric Table:")
    display(pivot)

    # 3. metric 별 성능 시각화
    for metric in metric_types:
        if metric in pivot.columns:
            pivot[metric].sort_values(ascending=False).plot(kind="bar", figsize=(10, 4), title=f"{results_path}: Model Comparison by {metric.upper()}")
            plt.ylabel(metric.upper())
            plt.tight_layout()
            plt.show()

    # 4. 중요도 이미지 시각화
    importance_imgs = glob.glob(os.path.join(results_path, "*", "importance.png"))
    for img_path in importance_imgs:
        model_name = os.path.basename(os.path.dirname(img_path))
        img = Image.open(img_path)
        plt.figure()
        plt.imshow(img)
        plt.axis("off")
        plt.title(f"{results_path} - {model_name} (Importance)")
        plt.show()

    # 5. 상관관계 히트맵
    corr_path = os.path.join(results_path, "correlation_matrix.csv")
    if os.path.exists(corr_path):
        corr_df = pd.read_csv(corr_path, index_col=0)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_df, annot=True, cmap="coolwarm")
        plt.title(f"{results_path} - Feature Correlation")
        plt.tight_layout()
        plt.show()
    else:
        print(" 상관관계 히트맵 없음.")


# ### Compete Mode

# In[150]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os
import glob

# 📁 Compete 모드에서 여러 metric 기준 실험한 폴더들 나열
results_folders = [
    "AutoML_results_compete_logloss",
    "AutoML_results_compete_f1",
    "AutoML_results_compete_auc",
    "AutoML_results_compete_accuracy",
    "AutoML_results_compete_precision",
    "AutoML_results_compete_recall"
]

for results_path in results_folders:
    if not os.path.exists(os.path.join(results_path, "leaderboard.csv")):
        print(f"[ X ] {results_path} → leaderboard.csv 없음. 건너뜁니다.")
        continue

    print(f"\nCOMPETE MODE 분석 중: {results_path}\n")

    # 1. 리더보드 불러오기
    leaderboard = pd.read_csv(os.path.join(results_path, "leaderboard.csv"))

    # 2. metric_type 종류 및 피벗 테이블 생성
    metric_types = leaderboard["metric_type"].unique()
    pivot = leaderboard.pivot_table(index=["name", "model_type"], 
                                     columns="metric_type", 
                                     values="metric_value")
    print("Metric Table:")
    display(pivot)

    # 3. metric별 성능 시각화
    for metric in metric_types:
        if metric in pivot.columns:
            pivot[metric].sort_values(ascending=False).plot(
                kind="bar", figsize=(10, 4),
                title=f"{results_path} - Model Comparison by {metric.upper()}"
            )
            plt.ylabel(metric.upper())
            plt.tight_layout()
            plt.show()

    # 4. 중요도 이미지 시각화 (있다면)
    importance_imgs = glob.glob(os.path.join(results_path, "*", "importance.png"))
    for img_path in importance_imgs:
        model_name = os.path.basename(os.path.dirname(img_path))
        img = Image.open(img_path)
        plt.figure()
        plt.imshow(img)
        plt.axis("off")
        plt.title(f"{results_path} - {model_name} (Importance)")
        plt.show()

    # 5. 상관관계 히트맵 출력 (있다면)
    corr_path = os.path.join(results_path, "correlation_matrix.csv")
    if os.path.exists(corr_path):
        corr_df = pd.read_csv(corr_path, index_col=0)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_df, annot=True, cmap="coolwarm")
        plt.title(f"{results_path} - Feature Correlation")
        plt.tight_layout()
        plt.show()
    else:
        print("상관관계 히트맵 없음.")


# In[151]:


# metric_type에 어떤 지표가 포함되어 있는지 확인
print("사용된 metric_type들:")
print(leaderboard['metric_type'].unique())


# In[152]:


print(leaderboard.columns)

