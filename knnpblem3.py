x=[[10,8],[7,9],[8,10],[7,3],[5,6],[7,5]]
y=['Outstanding','Outstanding','Outstanding','Good','Good','Good']
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x,y)
irreg=[[8,6]]
print(classifier.predict(irreg))