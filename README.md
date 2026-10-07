# Machine Learning Based Network Intrusion Detection

A machine learning-based network intrusion detection system using the **UNSW-NB15 dataset**, with a comparative analysis of **Logistic Regression, Random Forest, and XGBoost**.

## 📌 Project Overview

Network intrusion detection is an important cybersecurity task that involves identifying malicious network traffic from normal network activity.

This project applies supervised machine learning techniques to classify network traffic as either:

- **Normal**
- **Attack**

Three classification algorithms are trained and evaluated using the same preprocessing pipeline and official UNSW-NB15 train-test split. Their performance is compared using Accuracy, Precision, Recall, F1-Score, False Positives, and False Negatives.

## 🎯 Objectives

- Analyze network traffic data from the UNSW-NB15 dataset.
- Preprocess numerical and categorical network features.
- Compare multiple machine learning classification algorithms.
- Evaluate models using cybersecurity-relevant performance metrics.
- Identify the best-performing model for network intrusion detection.
- Analyze important features contributing to XGBoost predictions.
- Develop a foundation for a deployable intrusion detection application.

## 📊 Dataset

The project uses the **UNSW-NB15 dataset**, a widely used dataset for network intrusion detection research.

### Dataset Details

| Property | Value |
|---|---:|
| Training records | 175,341 |
| Testing records | 82,332 |
| Original columns | 36 |
| Model input features | 34 |
| Features after preprocessing | 186 |
| Target | Binary classification |
| Categorical features | `proto`, `service`, `state` |

The `label` column is used as the target variable, while `attack_cat` is excluded from the model inputs to avoid using target-derived information.

The official train-test split provided with the dataset is retained.

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

- Separation of features and target.
- Identification of numerical and categorical features.
- Standardization of numerical features using `StandardScaler`.
- One-hot encoding of categorical features using `OneHotEncoder`.
- Handling of unseen categorical values using `handle_unknown="ignore"`.
- Fitting preprocessing only on the training data.
- Applying the same transformation to the test data.

After preprocessing, the model receives **186 transformed features**.

## 🤖 Algorithms Used

### 1. Logistic Regression

Used as the baseline classification algorithm.

### 2. Random Forest

An ensemble learning method based on multiple decision trees. It is used to capture more complex patterns in network traffic.

### 3. XGBoost

A gradient boosting algorithm designed for efficient and powerful classification. It achieved the best overall performance among the evaluated models.

## 📈 Model Performance

| Algorithm | Accuracy | Precision | Recall | F1 Score | False Positives | False Negatives |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 79.69% | 74.16% | 96.85% | 84.00% | 15,296 | 1,427 |
| Random Forest | 86.56% | 81.73% | 97.35% | 88.86% | 9,865 | 1,202 |
| **XGBoost** | **86.98%** | **82.07%** | **97.71%** | **89.21%** | **9,677** | **1,040** |

### 🏆 Best Model

**XGBoost** achieved the best overall performance:

- Accuracy: **86.98%**
- Precision: **82.07%**
- Recall: **97.71%**
- F1 Score: **89.21%**
- False Negatives: **1,040**

Since false negatives are particularly important in intrusion detection, XGBoost's lower number of missed attack instances makes it the preferred model for this project.

## 🔍 Feature Importance

Feature importance analysis was performed using the trained XGBoost model.

The most important features included:

- `dload`
- `swin`
- `is_sm_ips_ports`
- `proto_arp`
- `sload`
- `tcprtt`
- `ackdat`
- `service_dns`
- `proto_tcp`

These features indicate that network traffic characteristics such as data load, sliding-window statistics, protocol information, and connection-related attributes contributed significantly to the model's classification decisions.

## 📊 Results

The project includes visual comparisons of:

- Classification algorithm performance
- False positives and false negatives
- Confusion matrices
- XGBoost feature importance

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Jupyter Notebook / Kaggle
- Streamlit
- Git & GitHub

## 📁 Project Structure

```text
network-intrusion-detection-ml/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── xgb_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   └── network-intrusion-detection.ipynb
│
└── images/
    ├── performance_comparison.png
    ├── fp_fn_comparison.png
    ├── confusion_matrix_comparison.png
    └── xgboost_feature_importance.png
