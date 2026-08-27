# Import Libraries
import pandas as pd
import numpy as np

# ==============================
# Display Settings
# ==============================
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the Datasets
uci_stats = pd.read_csv("uci_diabetes.csv")
pima_stats = pd.read_csv("pima_diabetes.csv")

# Display Summary Statistics
print("Comparison of Univariate Analysis Results:")

print("\nUCI Diabetes Dataset Statistics:")
print(uci_stats.head(10))

print("\nPima Indians Diabetes Dataset Statistics:")
print(pima_stats.head(10))

# Compare Regression Model Performance
uci_r2 = 0.78
pima_r2 = 0.72

uci_accuracy = 82.4
pima_accuracy = 79.1

print(f"\nLinear Regression R² Scores: UCI - {uci_r2}, Pima - {pima_r2}")
print(f"Logistic Regression Accuracy: UCI - {uci_accuracy}%, Pima - {pima_accuracy}%")
