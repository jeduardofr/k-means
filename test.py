from kmeans import KMeans
import pandas as pd

data = pd.read_csv("iris.csv")
without_class = data.drop(columns=["class"])

k = KMeans(clusters=3, rounds=6, iterations=100)
k.set_data(without_class)
k.solve()

for s in k.snapshots:
    print("# Iteraciones: {}".format(s['iterations']))
    nodes = s['data']
    for index in range(len(nodes)):
        pass
        # print("Clase {} => Agrupación {}".format(data["class"][index], nodes[index].centroid_id))
    print("==========")
