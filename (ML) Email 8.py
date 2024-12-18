
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('emails.csv')

df.isnull().sum()

x = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.30, random_state = 101)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)

cm

from sklearn.metrics import classification_report
cl_report=classification_report(y_test,y_pred)
print(cl_report)

print("Accuracy Score for KNN : ", accuracy_score(y_pred,y_test))

from sklearn.svm import SVC
svc = SVC(C=1.0,kernel='rbf',gamma='auto')
svc.fit(x_train,y_train)
y_pred2 = svc.predict(x_test)

cma = confusion_matrix(y_test, y_pred2)
cma

print("Accuracy Score for SVC : ", accuracy_score(y_pred2,y_test))

cl_report=classification_report(y_test,y_pred2)
print(cl_report)
