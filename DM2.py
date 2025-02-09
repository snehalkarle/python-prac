import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from sklearn.preprocessing import StandardScaler
# Set up Kaggle API credentials (update the path if needed)
os.environ['KAGGLE_CONFIG_DIR'] = "/path/to/kaggle.json"
# Initialize Kaggle API
api = KaggleApi()
api.authenticate()
df = pd.read_csv('Employee.csv')
# Inspect the first few rows
print("Cleaned dataset saved as 'Employee.csv':")
print(df.head())
# Drop duplicates
df = df.drop_duplicates()
# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median()) # Fill missing 'Age' with median
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0]) # Fill missing 'Embarked'with mode
# Convert categorical variables
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
# Drop irrelevant columns
df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)
# Normalize the 'Fare' column (optional)
scaler = StandardScaler()
df['Fare'] = scaler.fit_transform(df[['Fare']])
# Save cleaned dataset
df.to_csv('Employee.csv', index=False)
print("Cleaned dataset saved as 'Employee.csv'")
