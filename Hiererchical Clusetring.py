from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import  linkage,dendrogram
import numpy as np
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
np.set_printoptions(precision=5,suppress=True)
#generate Two Clusters

np.random.seed(4711)
a =np.random.multivariate_normal([10,0],[[3,1],[1,4]],size=[100,])
b =np.random.multivariate_normal([10,20],[[3,1],[1,4]],size=[50,])

x=np.concatenate((a,b),)

print(x.shape)
plt.scatter(x[:,0],x[:,1])

z=linkage(x,'ward')
c,coph_dist=cophenet(z,pdist(x))
print(c)
print(z[0])
print(z[1])
print('\n,\n')
print(z[:30])

plt.show()