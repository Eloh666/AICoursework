from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
import networkx as nx


class MatPlotLibRenderer(FigureCanvas):

    def __init__(self):
        super().__init__(Figure(tight_layout=True))
        self.axes = self.figure.add_subplot(111)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.name = "Cavern"

    def plotGraph(self, graph):
        pos = nx.fruchterman_reingold_layout(graph)
        self.axes.clear()
        self.axes.relim()
        self.axes.autoscale_view(True, True, True)
        self.draw_idle()
        nx.draw_networkx_nodes(graph, pos, ax=self.axes, node_color='b', alpha=0.5, node_size=3000)
        nx.draw_networkx_edges(graph, pos, ax=self.axes, arrows=True, alpha=0.1)
        nx.draw_networkx_labels(graph, pos, ax=self.axes, labels=nx.get_node_attributes(graph, 'coords'), font_size=16)
        nx.draw_networkx_edge_labels(graph, pos, ax=self.axes, alpha=0.1)
