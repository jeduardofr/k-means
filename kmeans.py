from random import seed, uniform
from node import Node

class KMeans():
    def __init__(self, clusters, rounds, iterations):
        self._n_clusters = clusters
        self._n_rounds = rounds
        self._n_iterations = iterations
        self.data = None
        self.snapshots = []

        self._n_attributes = None
        self._max_attributes = []
        self._min_attributes = []
        self._centroids = []

    def process_data(self, data):
        """
        Convert the DataFrame from pandas into an array of Nodes as rows
        """
        self._n_attributes = len(data.columns)
        attributes = data.columns
        res = []

        for i in range(len(data)):
            points = [data[attr][i] for attr in attributes]
            res.append(Node(points))

        return res

    def set_data(self, data):
        self.data = self.process_data(data)

        # Retrieve the maximum and minimum for each attribute in our data set
        self._max_attributes = [i for i in data.max()]
        self._min_attributes = [i for i in data.min()]

    def pick_random_centroids(self):
        self._centroids = []
        for _ in range(self._n_clusters):
            points = [
                uniform(self._min_attributes[i], self._max_attributes[i]) for i in range(self._n_attributes)
            ]
            self._centroids.append(Node(points))

    def solve(self):
        for i in range(self._n_rounds):
            self.pick_random_centroids()

            iterations = 0
            has_change = True

            while has_change is True and iterations <= self._n_iterations:
                iterations += 1
                for node in self.data:
                    node.choose_closest(self._centroids)

                has_change = not self.reubicate_centroids()

            self.snapshots.append({
                "data": self.data.copy(),
                "iterations": iterations
            })

    def reubicate_centroids(self):
        filter_by_id = lambda id, nodes : [node for node in nodes if node.centroid_id == id]
        changed = False

        for i in range(self._n_clusters):
            nodes = filter_by_id(i, self.data)
            total = len(nodes)
            avg = [0,0,0,0]
            for node in nodes:
                avg[0] += node.points[0]
                avg[1] += node.points[1]
                avg[2] += node.points[2]
                avg[3] += node.points[3]

            if total > 0:
                avg[0] = avg[0] / total
                avg[1] = avg[1] / total
                avg[2] = avg[2] / total
                avg[3] = avg[3] / total
            else:
                total = 1

            if (self._centroids[i].points[0] != avg[0] or self._centroids[i].points[1] != avg[1] or
                self._centroids[i].points[2] != avg[2] or self._centroids[i].points[3] != avg[3]):
                changed = True

            self._centroids[i].points = avg

        return changed
