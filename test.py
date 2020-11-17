from kmeans import KMeans
import pandas as pd

data = pd.read_csv("iris.csv")
without_class = data.drop(columns=["class"])

k = KMeans(clusters=3, rounds=5, iterations=100)
k.set_data(without_class)
k.solve()
for s in k.snapshots:
    print(s['iterations'])
