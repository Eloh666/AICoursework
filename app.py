import matplotlib
matplotlib.use("Qt5Agg")
from Parser import Parser
from Rendering.Renderer import MatPlotLibRenderer
from Algorithms import Dijkstra

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog
import sys

class AICourseWork(QMainWindow):
    def __init__(self):
        super(AICourseWork, self).__init__()
        uic.loadUi('GUI.ui', self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Speleologist")

        # Setup general state parameters
        self.currentNetwork = None

        # Setup rendering canvas
        self.layout = QVBoxLayout(self.graphWidget)
        self.renderingCanvas = MatPlotLibRenderer()
        self.layout.addWidget(self.renderingCanvas)

        #  Bindings
        # open file
        self.actionOpen.triggered.connect(self.openFile)
        # solve graph
        self.solveButton.clicked.connect(self.findShortestPath)

        self.testingOpen()

    def testingOpen(self):
        file = 'C:/Users/Eloh/Desktop/AICoursework/TestFiles/test.cav'
        self.currentNetwork = Parser.CavernsNetwork(file)
        self.renderingCanvas.plotGraph(self.currentNetwork.graph)

    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileNames()", directory='./TestFiles', filter='*.cav')
        if file:
            print(file)
            self.currentNetwork = Parser.CavernsNetwork(file)
            self.renderingCanvas.plotGraph(self.currentNetwork.graph)

    # solve with selected algorithm
    def findShortestPath(self):
        print(Dijkstra.bidirectionalDijkstra(self.currentNetwork.graph, 0, 6))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AICourseWork()
    window.show()
    sys.exit(app.exec_())
