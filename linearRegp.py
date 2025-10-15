from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the dataset
diabetes = load_diabetes()

# Step 2: Select one feature (e.g., BMI - body mass index)
X = diabetes.data[:, [2]]  # Feature at index 2 is 'bmi'
y = diabetes.target

# Step 3: Split data into training and testing sets (70% training, 30% testing)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Create and train the Linear Regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Step 5: Predict using the test data
y_pred = model.predict(x_test)

# Step 6: Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Step 7: Display results
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
print("Mean Squared Error:", mse)
print("R² Score:", r2)