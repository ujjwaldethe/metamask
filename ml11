
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("sales_data_sample.csv",encoding="latin")

x = df.iloc[:,[3,4]].values
wcss = [] #within cluster sum of square
for i in range(1,13):
#init argument is the method for initializing the centroid
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(x)
#we calculate wcss value for each k value
    wcss.append(kmeans.inertia_)
ks = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow method")
plt.xlabel("K value")
plt.ylabel("WCSS")

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
data = sc.fit_transform(x)

wcss =[]
for i in range(1,11):
    clustering = KMeans(n_clusters=i, init="k-means++", random_state=42)
    clustering.fit(data)
    wcss.append(clustering.inertia_)
ks = [1,2,3,4,5,6,7,8,9,10]
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow method")
plt.xlabel("K value")
plt.ylabel("WCSS")
