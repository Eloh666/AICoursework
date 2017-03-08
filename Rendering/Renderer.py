from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
import networkx as nx
import math


class MatPlotLibRenderer(FigureCanvas):

    def __init__(self):
        super().__init__(Figure(tight_layout=True))
        self.axes = self.figure.add_subplot(111)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.pos = None
        self.name = "Cavern"

    def clearFigure(self):
        self.pos = None
        self.axes.relim()
        self.axes.autoscale_view(True, True, True)
        self.draw_idle()

    def plotGraph(self, network, path=[]):

        graph = network.graph
        source = network.source
        target = network.target

        base = path == []
        nodesNum = len(graph.nodes())
        if not self.pos:
            self.pos = nx.fruchterman_reingold_layout(graph, scale=100, k=2 / math.sqrt(nodesNum))

        self.axes.clear()
        self.axes.relim()
        self.axes.autoscale_view(True, True, True)
        self.draw_idle()

        # sets how to mark edges
        source = [source]
        target = [target]
        if not base:
            path = [node for node in path if node not in source+target]
        regularNodes = [node for node in graph.nodes() if node not in path+source+target]

        nx.draw_networkx_nodes(graph,
                               self.pos,
                               nodelist=source,
                               ax=self.axes,
                               node_color='green',
                               alpha=0.5,
                               node_size=20000/nodesNum,
                               label='Source Node'
                               )
        nx.draw_networkx_nodes(graph,
                               self.pos,
                               nodelist=target,
                               ax=self.axes,
                               node_color='orange',
                               alpha=0.5,
                               node_size=20000/nodesNum,
                               label='Destination Node'
                               )
        nx.draw_networkx_nodes(graph,
                               self.pos,
                               nodelist=path,
                               ax=self.axes,
                               node_color='red',
                               alpha=0.5,
                               node_size=20000/nodesNum,
                               label='Selected Path' if not base else None
                               )
        nx.draw_networkx_nodes(graph,
                               self.pos,
                               nodelist=regularNodes,
                               ax=self.axes,
                               node_color='blue',
                               alpha= 0.5 if base else 0.1,
                               node_size=20000/nodesNum,
                               label='Others'
                               )

        nx.draw_networkx_edges(graph, self.pos, ax=self.axes, arrows=True, alpha=0.25)
        nx.draw_networkx_labels(graph, self.pos, ax=self.axes, labels=nx.get_node_attributes(graph, 'coords'), font_size=16)
        nx.draw_networkx_edge_labels(graph, self.pos, ax=self.axes, alpha=0.1)
        self.axes.legend(markerscale=1/5, title='Node types')
