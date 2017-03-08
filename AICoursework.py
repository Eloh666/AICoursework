from Parser import Parser
from Algorithms.Dijkstra import Dijkstra

file = 'C:/Users/Eloh/Desktop/AICoursework/TestFiles/test.cav'
currentNetwork = Parser.CavernsNetwork(file)
dijk = Dijkstra(currentNetwork, lambda x: print(x))
dijk.bidirectionalDijkstra()