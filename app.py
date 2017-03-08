import matplotlib
matplotlib.use("Qt5Agg")
from Parser import Parser
from Rendering.Renderer import MatPlotLibRenderer
from Algorithms import Dijkstra

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import sys

class AICourseWork(QMainWindow):
    def __init__(self):
        super(AICourseWork, self).__init__()
        uic.loadUi('GUI.ui', self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Setup general state parameters
        self.currentNetwork = None

        # Setup rendering canvas
        self.layout = QVBoxLayout(self.graphWidget)
        self.renderingCanvas = MatPlotLibRenderer()
        self.canvarToolbar = NavigationToolbar(self.renderingCanvas, parent=None)
        self.layout.addWidget(self.canvarToolbar)
        self.layout.addWidget(self.renderingCanvas)

        #  Bindings
        # open file
        self.actionOpen.triggered.connect(self.openFile)

        # solve graph
        self.solveButton.clicked.connect(self.findShortestPath)

        self.testingOpen()

    def testingOpen(self):
        file = 'C:/Users/Eloh/Desktop/AICoursework/TestFiles/test3.cav'
        self.currentNetwork = Parser.CavernsNetwork(file)
        self.renderingCanvas.plotGraph(self.currentNetwork)

    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileNames()", directory='./TestFiles', filter='*.cav')
        if file:
            self.currentNetwork = Parser.CavernsNetwork(file)
            self.renderingCanvas.clearFigure()
            self.activityLog.clear()
            self.renderingCanvas.plotGraph(self.currentNetwork)

    # solve with selected algorithm
    def findShortestPath(self):
        self.activityLog.clear()
        self.activityLog.insertPlainText('Processing ' + self.currentNetwork.fileName + '\n')
        result = Dijkstra.bidirectionalDijkstra(
            self.currentNetwork,
            lambda text: self.activityLog.insertPlainText('\n' + text)
        )
        distance, path = result
        self.renderingCanvas.plotGraph(self.currentNetwork, path)
        self.distanceLabel.setText('Total Distance ' + str(distance))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AICourseWork()
    window.show()
    sys.exit(app.exec_())
