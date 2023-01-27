from copy import deepcopy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv("C:\\Users\\panka\\Downloads\\DataSets\\iris.csv")
print(x.shape)
print((x.head()))

plt.rcParams['figure.figsize']=(8,5)
plt.style.use('ggplot')

v1 =x['sepal_length'].values
v2 =x['petal_length'].values

#print(v1,'\n')
#print(v2)

data =np.array(list(zip(v1,v2)))
#print(data)

plt.scatter(v1,v2,c='red',s=7)
#plt.show()

def dist(a,b,ax=1):
    return np.linalg.norm(a-b,axis=ax)

k =3
C_X =np.random.randint(0,int(np.max(data)-0.7),size=k)
C_Y =np.random.randint(0,int(np.max(data)-0.7),size=k)

data2 =np.array(list(zip(C_X,C_Y)),dtype=np.float32)

print(data2)


plt.scatter(v1,v2,c='green',s=7)
plt.scatter(C_X,C_Y,marker='*',s=200,c='blue')
plt.show()