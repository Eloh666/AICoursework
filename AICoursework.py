from Parser import Parser
from Algorithms.Dijkstra import Dijkstra
from Utils.UndoRedoStack import UndoRedoStack
import copy

file = 'C:/Users/Eloh/Desktop/AICoursework/TestFiles/test.cav'
currentNetwork = Parser.CavernsNetwork(file)
dijk = Dijkstra(currentNetwork, lambda x: print(x))
stack = UndoRedoStack()
stack.onChange(copy.deepcopy(dijk))