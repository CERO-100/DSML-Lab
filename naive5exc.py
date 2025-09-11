import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix
df=pd.read_excel("weather.xlsx")
print("Dataset:\n",df)
le=preprocessing.LabelEncoder()
weather_encoded=le.fit_transform(df['Weather'])
temp_encoded=le.fit_transform(df['Temp'])
label=le.fit_transform(df['Play'])
print("Weather Encoded:",weather_encoded)
print("Temp Encoded:",temp_encoded)
print("Play Encoded:",label)
features=list(zip(weather_encoded,temp_encoded))
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,2]])
print("Predicted Value:",predicted)
y_pred=model.predict(features)
print("Accuracy:",accuracy_score(label,y_pred))
print("Precision",precision_score(label,y_pred,average='binary'))
print("Confusion Matrix:\n",confusion_matrix(label,y_pred))