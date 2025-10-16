import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

data=pd.read_csv("data1.csv")
X=data[['gives_birth','aquatic_animal','aerial_animal','has_legs']]
y=data['class_label']
x_train , x_test, y_train, y_test=train_test_split(X , y , test_size=0.3 , random_state=1)
model=DecisionTreeClassifier(criterion='entropy',random_state=1)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)

print("Accuracy:",accuracy*100)
print("\nActual labels:",list(y_test))
print("Predicted labels:",list(y_pred)) 
plt.figure(figsize=(12,8))
tree.plot_tree(model,feature_names=['gives_birth','aquatic_animal','aerial_animal','has_legs'],class_names=model.classes_,filled=True,rounded=True)
plt.show()


