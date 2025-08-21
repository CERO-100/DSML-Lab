from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

# Input data
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Overcast','Overcast','Rainy']
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot']
play = ['No','No','Yes','Yes','Yes','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

# Encoding
le = preprocessing.LabelEncoder()
weather_encoded = le.fit_transform(weather)
print("Weather:", weather_encoded)

temp_encoded = le.fit_transform(temp)
print("Temp:", temp_encoded)

label = le.fit_transform(play)
print("Play:", label)

# Combine features
features = list(zip(weather_encoded, temp_encoded))
print("Features:", features)

# Train model
model = GaussianNB()
model.fit(features, label)

# Predict
predicted = model.predict([[0, 2]])  # Example: Sunny and Cool
print("Predicted Value:", predicted)
print("Predicted Label:", le.inverse_transform(predicted))