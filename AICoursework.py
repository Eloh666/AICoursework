from Parser import Parser
from Rendering import Renderer
import time

graph = Parser.GraphsParser('TestFiles/', 'test.cav').parseFile()
renderer = Renderer.GraphRenderer(graph)
for i in ['r', 'g', 'b', 'y']:
    renderer.plotGraph(i)

