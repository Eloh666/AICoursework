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

    def plotGraph(self, network, finalPath=[], primaryVisited=[], secondaryVisisted=[], noPath=False, final=False):

        graph = network.graph
        source = network.source
        target = network.target

        nodesNum = len(graph.nodes())
        if not self.pos:
            self.pos = nx.fruchterman_reingold_layout(graph, scale=100, k=2 / math.sqrt(nodesNum))

        self.axes.clear()
        self.axes.relim()
        self.draw_idle()

        # sets how to mark edges
        source = [source]
        target = [target]

        regularNodes = [node for node in graph.nodes() if
                        node not in source + target]

        if final:
            redEdges = list(
                filter(lambda x:
                       x[0] in finalPath and x[1] in finalPath
                       or
                       x[1] in finalPath and x[0] in finalPath, graph.edges())
            )
            finalPath = [node for node in finalPath if node not in source + target]
            regularNodes = [node for node in regularNodes if node not in finalPath]
        else:
            redEdges = list(
                filter(lambda x:
                       x[0] in primaryVisited and x[1] in secondaryVisisted
                       or
                       x[1] in primaryVisited and x[0] in secondaryVisisted, graph.edges())
            )
            regularNodes = [node for node in regularNodes if node not in primaryVisited + secondaryVisisted]
            source = [node for node in source if node not in primaryVisited + secondaryVisisted]
            target = [node for node in target if node not in primaryVisited + secondaryVisisted]

        regularEdges = [node for node in graph.edges() if node not in redEdges]

        # renders source, destination and general nodes
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
                               nodelist=regularNodes,
                               ax=self.axes,
                               node_color='grey' if noPath else 'blue',
                               alpha= 0.25,
                               node_size=20000/nodesNum,
                               label='Others'
                               )
        # renders the final path
        if final:
            nx.draw_networkx_nodes(graph,
                                   self.pos,
                                   nodelist=finalPath,
                                   ax=self.axes,
                                   node_color='red',
                                   alpha=0.5,
                                   node_size=20000 / nodesNum,
                                   label='Selected Path' if final else None
                                   )
        # otherwise renders the nodes currently being visited
        else:
            nx.draw_networkx_nodes(graph,
                                   self.pos,
                                   nodelist=secondaryVisisted,
                                   ax=self.axes,
                                   node_color='yellow',
                                   alpha=0.5 if not final else 0.1,
                                   node_size=20000 / nodesNum,
                                   label='Secondary Visisted'
                                   )
            nx.draw_networkx_nodes(graph,
                                   self.pos,
                                   nodelist=primaryVisited,
                                   ax=self.axes,
                                   node_color='purple',
                                   alpha=0.5 if not final else 0.1,
                                   node_size=20000 / nodesNum,
                                   label='Primary Visited'
                                   )

        # Renderes red edges
        nx.draw_networkx_edges(graph,
                               self.pos,
                               edgelist=regularEdges,
                               ax=self.axes,
                               arrows=True,
                               alpha=0.25,
                               edge_color='red' if noPath else 'black'
                               )

        # Renders black edges
        nx.draw_networkx_edges(graph,
                               self.pos,
                               edgelist=redEdges,
                               ax=self.axes,
                               arrows=True,
                               alpha=0.5,
                               edge_color='red'
                               )
        nx.draw_networkx_labels(graph, self.pos, ax=self.axes, labels=nx.get_node_attributes(graph, 'coords'), font_size=16)
        nx.draw_networkx_edge_labels(graph, self.pos, ax=self.axes, alpha=0.1)
        self.axes.legend(markerscale=1/5, title='Node types')
