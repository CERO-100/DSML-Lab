import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

# Step 1: Load dataset
data = pd.read_csv("data1.csv")

# Step 2: Separate features (X) and target (y)
X = data[['gives_birth', 'aquatic_animal', 'aerial_animal', 'has_legs']]
y = data['class_label']

# Step 3: Split into training and testing data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Step 4: Create Decision Tree model
model = DecisionTreeClassifier(criterion='entropy', random_state=1)
model.fit(x_train, y_train)

# Step 5: Predict using test data
y_pred = model.predict(x_test)

# Step 6: Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree Model Accuracy:", accuracy)

# Step 7: Display Predictions
print("\nActual labels:", list(y_test))
print("Predicted labels:", list(y_pred))

# Step 8: Visualize the Decision Tree
plt.figure(figsize=(12,8))
tree.plot_tree(model, feature_names=['gives_birth', 'aquatic_animal', 'aerial_animal', 'has_legs'],class_names=model.classes_, filled=True, rounded=True)
plt.show()