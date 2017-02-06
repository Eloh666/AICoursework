import networkx as nx
import matplotlib.pyplot as plt
import time

class GraphRenderer:

    def __init__(self, graph):
        self.graph = graph
        self.plot = plt

    def getPlot(self):
        return self.plot

    def plotGraph(self, color):
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_nodes(self.graph, pos, cmap=self.plot.get_cmap('jet'), node_color=color)
        nx.draw_networkx_edges(self.graph, pos, arrows=True)
        nx.draw_networkx_labels(self.graph, pos, labels=nx.get_node_attributes(self.graph, 'coords'))
