from Parser import Parser
from Algorithms import Dijkstra

file = 'C:/Users/Eloh/Desktop/AICoursework/TestFiles/test3.cav'
currentNetwork = Parser.CavernsNetwork(file)
print(Dijkstra.bidirectionalDijkstra(currentNetwork.graph, currentNetwork.source, currentNetwork.target))