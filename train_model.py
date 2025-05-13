import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib  # or use pickle

# ✅ Load dataset
try:
    data = pd.read_csv("insurance.csv")
    print("✅ Data loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load data: {e}")
    exit()

# ✅ Preprocessing
data = pd.get_dummies(data, drop_first=True)

X = data.drop("charges", axis=1)
y = data["charges"]

# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = LinearRegression()
model.fit(X_train, y_train)
print("✅ Model trained.")

# ✅ Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"📊 Model MSE: {mse:.2f}")

# ✅ Save model
model_dir = "saved_models"
model_path = os.path.join(model_dir, "model.pkl")

# 👉 Make sure folder exists
try:
    os.makedirs(model_dir, exist_ok=True)
except Exception as e:
    print(f"❌ ERROR: Could not create directory '{model_dir}' – {e}")
    exit()

try:
    joblib.dump(model, model_path)
    print(f"✅ Model saved at: {os.path.abspath(model_path)}")
except Exception as e:
    print(f"❌ ERROR: Failed to save model! {e}")
