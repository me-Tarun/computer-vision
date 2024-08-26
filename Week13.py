import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
iris = load_iris()
X = iris.data
Y = iris.target
pca = PCA(n_components= 2)
X_pca = pca.fit_transform(X)
plt.figure(figsize=(8,6))
for target,target_name in enumerate(iris.target_names):
    plt.scatter(X[Y == target,0],X[Y == target,1],label = target_name)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('original.iris Dataset(20)')
plt.legend()
plt.show()
plt.figure(figsize=(8,6))
for target,target_name in enumerate(iris.target_names):
    plt.scatter(X_pca[Y == target,0],X_pca[Y == target,1],label = target_name)
plt.xlabel('principal component 1')
plt.ylabel('principal component 2')
plt.title('Iris Dataset after PCA(2D)')
plt.legend()
plt.show()