from Parser import Parser
from Algorithms import Dijkstra

file = 'C:/Users/Eloh/Desktop/AICoursework/TestFiles/test.cav'
currentNetwork = Parser.CavernsNetwork(file)
print(Dijkstra.bidirectionalDijkstra(currentNetwork.graph, 0, 6))