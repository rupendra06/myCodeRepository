# 1. Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 2. Load the Dataset
df = pd.read_excel('C:\Users\RADHE\PythonCode\Titanic-Dataset.xlsx')  # Adjust path if needed

# 3. Basic Exploration
print(df.info())
print(df.describe())
print("Missing Values:\n", df.isnull().sum())

# 4. Handle Missing Values
df['Age'] = df['Age'].fillna(df['Age'].median())                 # Median for Age
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0]) # Mode for Embarked
df = df.drop(columns=['Cabin'])                                   # Drop Cabin (too many nulls)

# 5. Encode Categorical Variables
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])  # male=1, female=0
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)  # One-hot encoding

# 6. Normalize Numerical Features
scaler = StandardScaler()
num_cols = ['Age', 'Fare', 'SibSp', 'Parch']
df[num_cols] = scaler.fit_transform(df[num_cols])

# 7. Remove Outliers using IQR
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[~((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]

df = remove_outliers_iqr(df, 'Age')
df = remove_outliers_iqr(df, 'Fare')

# 8. Final Check
print("\n✅ Cleaned DataFrame Info:\n")
print(df.info())
print(df.head())

# 9. Save Cleaned Data
df.to_csv('Cleaned_Titanic_Dataset.csv', index=False)
print("\n✅ Cleaned dataset saved to: Cleaned_Titanic_Dataset.csv")
print("Successful")
