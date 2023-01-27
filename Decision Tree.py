import pydotplus
from sklearn import tree
import collections

x = [[180,15,1],
     [177,40,0],
     [136,35,1],
     [174,65,0],
     [148,20,1],
     [181,70,1]]

y =['approved','disapproved','approved','disapproved','approved','disapproved']

feature_names = ['grade', 'fitness','voice_pitch']
#Training the model

clf =tree.DecisionTreeClassifier()
clf =clf.fit(x,y)

#Visualize the data

dot_data =tree.export_graphviz(clf,feature_names=feature_names,out_file=None,filled=True,rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data)

colors =('red','blue')
edges =collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

for edge in edges:
    edges[edge].sort()
    for i in range(2):
        dest =graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png("Decision Tree.png")
clf.fit(x,y)
predict = clf.predict([[190,66,0]])
print(predict)