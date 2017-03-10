import sys
import matplotlib
matplotlib.use("Qt5Agg")
from Parser import Parser
from Rendering.Renderer import MatPlotLibRenderer
from Algorithms.Dijkstra import Dijkstra
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog
from Utils.UndoRedoStack import UndoRedoStack


class AICourseWork(QMainWindow):
    def __init__(self):
        super(AICourseWork, self).__init__()
        uic.loadUi('GUI.ui', self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Setup general state parameters
        self.stack = UndoRedoStack()
        self.currentNetwork = None
        self.algorithmWrapper = None

        # Setup rendering canvas
        self.layout = QVBoxLayout(self.graphWidget)
        self.renderingCanvas = MatPlotLibRenderer()
        self.canvarToolbar = NavigationToolbar(self.renderingCanvas, parent=None)
        self.layout.addWidget(self.canvarToolbar)
        self.layout.addWidget(self.renderingCanvas)

        #  Bindings
        # open file
        self.actionOpen.triggered.connect(self.openFile)

        # bind buttons graph
        self.solveButton.clicked.connect(self.findShortestPath)
        self.stepButton.clicked.connect(self.stepThrough)
        self.undoButton.clicked.connect(self.undo)
        self.redoButton.clicked.connect(self.redo)
        self.testingOpen()

        self.undoButton.setEnabled(False)
        self.redoButton.setEnabled(False)

    def undo(self):
        _, past, present = self.stack.undo()
        self.undoButton.setEnabled(past)
        self.redoButton.setEnabled(present)

    def redo(self):
        _, past, present = self.stack.redo()
        self.undoButton.setEnabled(past)
        self.redoButton.setEnabled(present)

    def testingOpen(self):
        file = 'C:/Users/Eloh/Desktop/AICoursework/TestFiles/test3.cav'
        self.currentNetwork = Parser.CavernsNetwork(file)
        self.renderingCanvas.plotGraph(self.currentNetwork)
        self.algorithmWrapper = Dijkstra(
            network=self.currentNetwork,
            log=lambda text: self.activityLog.insertPlainText('\n' + text),
            renderer=self.renderingCanvas
            )

    def openFile(self):
        dialog = QFileDialog()
        file, _ = dialog.getOpenFileName(self, directory='./TestFiles', filter='*.cav')
        if file:
            self.stack.clearStack()
            self.currentNetwork = Parser.CavernsNetwork(file)
            self.renderingCanvas.clearFigure()
            self.activityLog.clear()
            self.algorithmWrapper = Dijkstra(
                network=self.currentNetwork,
                log=lambda text: self.activityLog.insertPlainText('\n' + text),
                renderer=self.renderingCanvas
            )
            self.stack.onChange(self.algorithmWrapper)
            self.stepButton.setEnabled(not self.algorithmWrapper.finished)
            self.distanceLabel.setText('Total Distance ')

    def stepThrough(self):
        distance = self.algorithmWrapper.bidirectionalDijkstra(stepping=True)
        self.stepButton.setEnabled(not self.algorithmWrapper.finished)
        _, past, present = self.stack.onChange(self.algorithmWrapper)
        self.undoButton.setEnabled(past)
        self.redoButton.setEnabled(present)
        if distance:
            self.distanceLabel.setText('Total Distance ' + str(distance))

    # solve with selected algorithm
    def findShortestPath(self):
        self.activityLog.clear()
        self.activityLog.insertPlainText('Processing ' + self.currentNetwork.fileName + '\n')
        distance = self.algorithmWrapper.bidirectionalDijkstra()
        self.distanceLabel.setText('Total Distance ' + str(distance))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AICourseWork()
    window.show()
    sys.exit(app.exec_())
