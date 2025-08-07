x=[[167,51],[187,62],[176,69],[173,64],[172,65],[174,56],[169,58],[173,57],[170,55],[169,53]]
y=['Underweight','Normal','Normal','Normal','Normal','Underweight','Normal','Normal','Normal','Underweight']
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=1)
classifier.fit(x,y)
anon=[[173,57]]
print(classifier.predict(anon))
