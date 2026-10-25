import pandas as pd
import numpy as np

# 1. Create a sample DataFrame with missing values (NaN) and duplicates
data = {
    'Student': ['Amit', 'Bhavna', 'Chetan', 'Diya', 'Amit', 'Esha', 'Farhan'],
    'Maths': [75, 82, np.nan, 90, 75, 72, 85],
    'Python': [80, 78, 70, 92, 80, np.nan, 88],
    'Attendance': [85, 90, 78, 95, 85, 80, np.nan],
    'City': ['Pune', 'Mumbai', 'Pune', 'Nashik', 'Pune', 'Mumbai', 'Pune']
}

df = pd.DataFrame(data)

print("--- 1. Original Dataset ---")
print(df)
print("\nDataset Information:")
print(df.info())

# 2. Check for missing values
print("\n--- 2. Checking Missing Values Count ---")
print(df.isnull().sum())

# 3. Handle missing values using fillna()
# Fill missing Maths and Attendance with mean, and Python with median
df['Maths'] = df['Maths'].fillna(df['Maths'].mean())
df['Python'] = df['Python'].fillna(df['Python'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())

print("\n--- 3. Dataset After Handling Missing Values ---")
print(df)

# 4. Identify and remove duplicate records
print("\n--- 4. Duplicate Rows Found ---")
print(df[df.duplicated()])

# Remove duplicates
df = df.drop_duplicates()
print("\n--- Dataset After Removing Duplicates ---")
print(df)

# 5. Data selection and filtering using loc[]
print("\n--- 5. Filtered Data (Students from Pune with Maths > 75) ---")
filtered_df = df.loc[(df['City'] == 'Pune') & (df['Maths'] > 75)]
print(filtered_df)