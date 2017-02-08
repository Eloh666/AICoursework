import networkx as nx
import matplotlib.pyplot as plt

class GraphRenderer:

    def __init__(self, graph):
        self.graph = graph
        self.plot = plt
        self.pos = nx.spring_layout(self.graph)


    def plotGraph(self, color):
        self.plot.show(block=False)
        nx.draw_networkx_nodes(self.graph, self.pos, cmap=self.plot.get_cmap('jet'), node_color=color)
        nx.draw_networkx_edges(self.graph, self.pos, arrows=True)
        nx.draw_networkx_labels(self.graph, self.pos, labels=nx.get_node_attributes(self.graph, 'coords'))
