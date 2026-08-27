import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('iris_dataset.csv')

# Display basic information and summary statistics
print("Basic Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Perform univariate analysis - species count
print("\nSpecies Count:")
print(df['species'].value_counts())

# Histogram
df.hist(figsize=(8,6), edgecolor='black')
plt.suptitle("Feature Distributions")
plt.show()

# Boxplot for Sepal Length
sns.boxplot(data=df, x='species', y='sepal length (cm)')
plt.title('Sepal Length Comparison')
plt.show()

# Pairplot to analyze feature relationships
sns.pairplot(df, hue='species')
plt.show()
