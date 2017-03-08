import numpy
import networkx as nx
import math
import ntpath

def euclideanDistance(a, b):
    x = pow(a[0] - b[0], 2)
    y = pow(a[1] - b[1], 2)
    return math.sqrt(x+y)

class CavernsNetwork:

    def __init__(self, fileName):
        self.fileName = ntpath.basename(fileName)

        # Parses basic file into a graph
        self.coordinates = []
        self.__cavernData = self.__readFile(fileName).split(',')
        self.__numberCoordinats = int(self.__cavernData[0], 10)

        # Selects source and destination
        self.source = 0
        self.target = self.__numberCoordinats - 1

        # Generates advanced structures from the data
        self.graph = self.__parseGraph()
        self.matrix = self.__parseMatrix()
        self.__computeEdges()

    def __readFile(self, fileName):
        with open(fileName, 'r') as cavernsFile:
            return cavernsFile.read().replace('\n', '')

    def __parseGraph(self):
        coordsData = self.__cavernData[1: (2 * self.__numberCoordinats) + 1]
        parsedCoordsData = list(map(lambda x: int(x, 10), coordsData))
        self.coordinates = list(zip(parsedCoordsData, parsedCoordsData[1:]))[::2]

        graph = nx.DiGraph()
        for index, value in enumerate(self.coordinates):
                graph.add_node(index, coords=tuple(numpy.squeeze(numpy.asarray(value))))
        return graph

    def __computeEdges(self):
        for (x, y), value in numpy.ndenumerate(self.matrix):
            if int(value) == 1:
                source = self.coordinates[x]
                dest = self.coordinates[y]
                self.graph.add_edge(
                    y,
                    x,
                    weight=round(euclideanDistance(source, dest), 2)
                )

    def __parseMatrix(self):
        matrixData = self.__cavernData[(2 * self.__numberCoordinats) + 1:]
        return numpy.matrix(matrixData).reshape(self.__numberCoordinats, self.__numberCoordinats)


