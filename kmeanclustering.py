# Import necessary libraries
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # features (sepal length, sepal width, petal length, petal width)

# Step 2: Create a DataFrame for better visualization
df = pd.DataFrame(X, columns=iris.feature_names)

# Step 3: Apply K-Means Clustering
# We know there are 3 species in Iris → so we choose 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Step 4: Add cluster labels to DataFrame
df['Cluster'] = kmeans.labels_

# Step 5: Display cluster centers and labels
print("Cluster Centers:\n", kmeans.cluster_centers_)
print("\nCluster Labels:\n", kmeans.labels_)

# Step 6: Visualize the Clusters (using 2 features for simplicity)
plt.scatter(X[:, 2], X[:, 3], c=kmeans.labels_, cmap='rainbow')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('K-Means Clustering on Iris Dataset')
plt.show()