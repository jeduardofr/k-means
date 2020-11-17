from math import sqrt

class Node():
    def __init__(self, points, centroid_id = None):
        self.points = points
        self.centroid_id  = centroid_id

    def distance_to(self, node):
        return (
            (self.points[0] - node.points[0])**2 +
            (self.points[1] - node.points[1])**2 +
            (self.points[2] - node.points[2])**2 +
            (self.points[3] - node.points[3])**2)

    def choose_closest(self, centroids):
        closer, id = self.distance_to(centroids[0]), 0

        for index in range(len(centroids)):
            distance = self.distance_to(centroids[index])
            if distance < closer:
                closer, id = distance, index

        self.centroid_id = id

    def __str__(self):
        numbers_str = ", ".join(str(x) for x in self.points)
        return "[{}] -> {}".format(numbers_str, self.centroid_id)

    def __repr__(self):
        return self.__str__()
