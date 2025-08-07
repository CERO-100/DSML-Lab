x=[[10,9],[1,4],[10,1],[7,10],[3,10],[1,1]]
y=['fruit','protein','fruit','vegetable','vegetable','protein']
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x,y)
tomato=[[6,4]]
print(classifier.predict(tomato))
carrot=[[4,9]]
print(classifier.predict(carrot))