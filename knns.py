from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Create the dataset
# Features: [Sweetness, Crunchiness]
X = [
    [10, 9],  # Apple
    [1, 4],   # Bacon
    [10, 1],  # Banana
    [7, 10],  # Carrot
    [3, 10],  # Celery
    [1, 1],   # Cheese
    [8, 5],   # Grape
    [3, 7],   # Green bean
    [3, 6],   # Nuts
    [7, 3]    # Orange
]

# Labels (Food Type)
y = [
    'Fruit', 
    'Protein', 
    'Fruit', 
    'Vegetable', 
    'Vegetable', 
    'Protein', 
    'Fruit', 
    'Vegetable', 
    'Protein', 
    'Fruit'
]

# Step 2: Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Create and train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

# Step 4: Predict on test data
y_pred = knn.predict(x_test)

# Step 5: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Step 6: Predict for a tomato (Sweetness=6, Crunchiness=4)
tomato_prediction = knn.predict([[6, 4]])
print("Predicted food type for Tomato:", tomato_prediction[0])