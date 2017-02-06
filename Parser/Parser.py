import os
import numpy
import networkx as nx

class GraphsParser:

    def __init__(self, filePath, fileName):
        self.fileName = fileName
        self.filePath = filePath

    def readFile(self):
        fullPath = os.path.abspath(self.filePath + self.fileName)
        with open(fullPath, 'r') as cavernsFile:
            return cavernsFile.read().replace('\n', '')

    def parseGraph(self, numNodes, list):

        graph = nx.DiGraph()
        data = numpy.matrix(list).reshape(numNodes, 2)
        for index, value in enumerate(data):
            graph.add_node(index, coords=tuple(numpy.squeeze(numpy.asarray(value))))
        return graph

    def parseMatrix(self, list):
        return numpy.matrix(list).reshape(7, 7)

    def computeEdges(self, graph, matrix):
        for (x, y), value in numpy.ndenumerate(matrix):
            if int(value) == 1:
                graph.add_edge(y, x)


    def parseFile(self):
        cavernData = self.readFile().split(',')
        if not cavernData or len(cavernData) < 1:
            return None
        numberCoordinats = int(cavernData[0], 10)
        coordsData = cavernData[1: (2 * numberCoordinats) + 1]
        matrixData = cavernData[(2 * numberCoordinats) + 1:]

        matrix = self.parseMatrix(matrixData)
        graph = self.parseGraph(numberCoordinats, coordsData)

        self.computeEdges(graph, matrix)
        return graph