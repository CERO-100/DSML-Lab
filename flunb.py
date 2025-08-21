from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
chills=['Yes','Yes','Yes','No','No','No','No','Yes']
runny_nose=['No','Yes','No','Yes','No','Yes','Yes','Yes']
headache=['Mild','No','Strong','Mild','No','Strong','Strong','Mild']
fever=['Yes','No','Yes','Yes','No','Yes','No','Yes']
flu=['No','Yes','Yes','Yes','No','Yes','No','Yes']
from heapq import merge 
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
chill_encoded=le.fit_transform(chills)
print("Chills:",chill_encoded)
runny_nose_encoded=le.fit_transform(runny_nose)
print("Runny Nose:",runny_nose_encoded)
headache_encoded=le.fit_transform(headache)
print("Headache:",headache_encoded)
fever_encoded=le.fit_transform(fever)
print("Fever:",fever_encoded)
label=le.fit_transform(flu)
print("Flu:",label)
features=list(zip(chill_encoded,runny_nose_encoded,headache_encoded,fever_encoded))
print(features)
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,1,2,1]])
print("Predicted value:",predicted)
print(le.inverse_transform(predicted))
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix
y_pred=model.predict(features)
acc=accuracy_score(label,y_pred)
prec=precision_score(label,y_pred,average='binary')
rec=recall_score(label,y_pred,average='binary')
print("Accuracy:",acc)
print("Precison:",prec)
print("Recall:",rec)
cm=confusion_matrix(label,y_pred)
print("Confusion Matrix:\n",cm)
