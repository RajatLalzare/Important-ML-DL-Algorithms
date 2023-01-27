import numpy as np
from sklearn.neighbors import NearestNeighbors

x =np.array([[-1,2],[4,2],[-2,1],[3,4],[-1,3],[-3,2],[-1,4]])

nb =NearestNeighbors(n_neighbors=3,algorithm='ball_tree').fit(x)

distance,indices =nb.kneighbors(x)

print(indices)
print(nb.kneighbors([[-1,3]]))