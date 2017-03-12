from heapq import heappush
from itertools import count

class AlgorithmWrapper:
    def __init__(self, network, log, weight='weight', renderer=None):
        self.renderer = renderer
        self.weight = weight
        self.log = log
        self.network = network
        self.graph = network.graph
        self.source = network.source
        self.target = network.target
        self.coordinates = network.coordinates
        self.__setupInitialParams()

        self.dirEnum = {
            0: 'forward',
            1: 'backward',
        }

    def __setupInitialParams(self):
        self.dists = {
            'forward': {},
            'backward': {},
        }

        # stores the available paths
        self.paths = {
            'forward': {self.source: [self.source]},
            'backward': {self.target: [self.target]},
        }

        # heap of (distance, node) tuples for extracting next node to expand
        self.fringe = {
            'forward': [],
            'backward': [],
        }

        # nodes who have already been seen and investigated
        self.visited = {
            'forward': {self.source: 0},
            'backward': {self.target: 0},
        }

        # neighs for extracting correct neighbor information
        # the method unwraps the successors to a node
        self.neighs = {
            'forward': self.graph.successors_iter,
            'backward': self.graph.predecessors_iter,
        }

        self.c = count()

        # setup the self.fringe heap
        heappush(self.fringe['forward'], (0, next(self.c), self.source))
        heappush(self.fringe['backward'], (0, next(self.c), self.target))

        # variables to hold shortest discovered path
        self.finalPath = []
        self.directionNum = 1
        self.finalDist = 0

        self.primaryVisited = []
        self.secondaryVisited = []
        self.noPath = False
        self.finished = False

    def restart(self):
        self.__setupInitialParams()

    def reRender(self):
        self.renderer.plotGraph(
            network=self.network,
            primaryVisited=self.primaryVisited,
            secondaryVisisted=self.secondaryVisited,
            noPath=self.noPath,
            finalPath=self.finalPath,
            final=self.finished
        )