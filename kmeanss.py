

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset=pd.read_csv('Customers.csv')

X=dataset.iloc[:,[3,4]].values

print(X)



#Using the elbow method to find the optimal number of clusters

from sklearn.cluster import KMeans

wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++',random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


plt.scatter(X[:,0],X[:,1],s=100,c='red')
plt.title('Without Clustering')
plt.xlabel('Annual Income(K$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()

#Fitting K-MEans to the dataset
kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(X)

dataset['cluster'] = y_kmeans
color=['blue','green','cyan','red','magenta']
for k in range(5):
    df = dataset[dataset['cluster']==k]
    plt.scatter(df['Annual Income (k$)'],df['Spending Score (1-100)'],s=100,c=color[k],label='Cluster'+str(k))
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income(K$)')
plt.ylabel('Spending Score(1-100)')
plt.show()
#Visualize the clusters
# plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=100,c='red',label='Cluster1')
# plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=100,c='blue',label='Cluster2')
# plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=100,c='green',label='Cluster3')
# plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=100,c='cyan',label='Cluster4')
# plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=100,c='magenta',label='Cluster5')







plt.figure(figsize=(12,7))
size_array = list(dataset.groupby(['cluster']).count()['Annual Income (k$)'].values)
print("size_array", size_array)
axis = sns.barplot(x=np.arange(0,5,1),y=size_array)
x=axis.set_xlabel("Cluster Number")
x=axis.set_ylabel("Annual Income(K$)")
plt.show()

df_cluster = dataset[dataset['cluster']==size_array.index(sorted(size_array)[0])].sample(5)

print(df_cluster)
























