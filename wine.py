import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Load the wine dataset
wine_bunch = load_wine()
wine = pd.DataFrame(wine_bunch.data, columns=wine_bunch.feature_names)
wine['target'] = wine_bunch.target
wine['target'] = wine['target'].map(dict(enumerate(wine_bunch.target_names)))

# 1. Shape and first 5 rows
print("Shape of dataset:", wine.shape)
print("\nFirst 5 Rows:")
print(wine.head())

# 2. Basic info
print("\nData Types and Non-Nulls:")
print(wine.info())

# 3. Summary statistics
print("\nSummary Statistics:")
print(wine.describe())

# 4. Missing values
print("\nMissing values:")
print(wine.isnull().sum())

# 5. Class distribution
print("\nClass Distribution")
print(wine['target'].value_counts())

# 6. Pairplot
sns.pairplot(wine, hue='target', diag_kind='kde')
plt.suptitle("Pairplot of Wine Features", y=1.02)
plt.show()

# 7. Correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(wine.drop('target', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Matrix")
plt.show()

# 8. Boxplots
plt.figure(figsize=(14, 6))
sns.boxplot(data=wine.drop('target', axis=1))
plt.xticks(rotation=90)
plt.title("Boxplot for Each Feature")
plt.tight_layout()
plt.show()
