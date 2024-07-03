import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from functions.functions import order_cluster

# Cargar datos desde el archivo CSV
rfm = pd.read_csv('./datasets/intermediate/rfm.csv')

# Seleccionar las características para clustering
features = rfm[['recency','frequency','monetary']]

# Método del codo para encontrar el número óptimo de clusters
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(features)
    sse.append(kmeans.inertia_)

# Graficar SSE frente al número de clusters
plt.plot(range(1, 11), sse, marker='o')
plt.xlabel('Número de Clusters')
plt.ylabel('SSE')
plt.title('Método del Codo')
plt.show()

# Aplicar K-means con el número óptimo de clusters (4 clusters)
kmeans = KMeans(n_clusters=4, random_state=0).fit(features)
rfm['cluster'] = kmeans.labels_

# Ordenar los clusters basados en la media de 'monetary'
rfm_kmeans = order_cluster('cluster', 'monetary', rfm, ascending=True)

# Guardar el dataset como csv
rfm_kmeans.to_csv('./datasets/intermediate/rfm_kmeans.csv', index=False)

