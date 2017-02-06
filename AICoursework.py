from Parser import Parser
from Rendering import Renderer
import time

parser = Parser.GraphsParser('TestFiles/', 'test.cav')
graph = parser.parseFile()
renderer = Renderer.GraphRenderer(graph)
plot = renderer.getPlot()
plot.show(block=False)
for i in ['r', 'g', 'b', 'y']:
    renderer.plotGraph(i)
    plot.pause(1)
plot.ioff()
plot.show(block=True)
