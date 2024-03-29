![CCFD](https://github.com/SanjayBharathi18/Portfolio_Projects/assets/165292172/e8ff1921-8bdb-4560-8b12-c335c261fa10)

# CREDIT CARD FRAUD DETECTION

The dataset contains transactions made by credit cards in September 2013 by European cardholders.This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.


## Sampling Technique

The dataset is highly imbalanced, with the positive class (frauds) accounting for 0.17% of all transactions. To address the aforementioned issue, we utilised some sampling approaches:

- RandomUnderSampling
- SMOTE (Synthetic Minority Over-sampling Technique)

## Accuracy Scores

SMOTE technique has higher evaluation scores than RandomUnderSampling technique.

RandomUnderSampling (Random Forest model) :
 - Accuracy : 96.08%
 - Precision : 96.16%
 - Recall : 96.08%

SMOTE (XGBoost model) :
 - Accuracy : 99.97%
 - Precision : 99.97%
 - Recall : 99.96%