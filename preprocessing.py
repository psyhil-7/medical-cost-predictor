import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the dataset
df = pd.read_csv("insurance.csv")  # Update with your dataset filename

# Step 1: Check for missing values
print(df.isnull().sum())  # Shows if any missing values exist

# Step 2: Convert categorical variables into numeric
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})

# One-hot encoding for 'region'
df = pd.get_dummies(df, columns=['region'], drop_first=True)

# Step 3: Split features (X) and target variable (y)
X = df.drop("charges", axis=1)  # All columns except 'charges'
y = df["charges"]  # Target variable

# Step 4: Normalize numerical features (age, bmi, children)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Split into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("Preprocessing Complete ✅")
