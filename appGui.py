# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Coursework(object):
    def setupUi(self, Coursework):
        Coursework.setObjectName("Coursework")
        Coursework.resize(1639, 897)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Coursework.sizePolicy().hasHeightForWidth())
        Coursework.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        Coursework.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Coursework)
        self.centralwidget.setObjectName("centralwidget")
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton.setGeometry(QtCore.QRect(1510, 110, 111, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/apple-touch-icon@2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.solveButton.setIcon(icon)
        self.solveButton.setIconSize(QtCore.QSize(40, 44))
        self.solveButton.setObjectName("solveButton")
        self.algorithmsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.algorithmsComboBox.setEnabled(False)
        self.algorithmsComboBox.setGeometry(QtCore.QRect(1340, 10, 261, 22))
        self.algorithmsComboBox.setObjectName("algorithmsComboBox")
        self.algorithmsComboBox.addItem("")
        self.twoWayCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.twoWayCheckBox.setEnabled(False)
        self.twoWayCheckBox.setGeometry(QtCore.QRect(1340, 40, 111, 17))
        self.twoWayCheckBox.setChecked(True)
        self.twoWayCheckBox.setObjectName("twoWayCheckBox")
        self.graphWidget = QtWidgets.QWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(20, 10, 1300, 841))
        self.graphWidget.setObjectName("graphWidget")
        self.activityLog = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.activityLog.setGeometry(QtCore.QRect(1340, 180, 281, 641))
        self.activityLog.setReadOnly(True)
        self.activityLog.setPlaceholderText("")
        self.activityLog.setObjectName("activityLog")
        self.Loglabel = QtWidgets.QLabel(self.centralwidget)
        self.Loglabel.setGeometry(QtCore.QRect(1340, 160, 261, 16))
        self.Loglabel.setObjectName("Loglabel")
        self.distanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.distanceLabel.setGeometry(QtCore.QRect(1340, 830, 261, 16))
        self.distanceLabel.setObjectName("distanceLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1330, 60, 291, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.undoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/002-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon1)
        self.undoButton.setIconSize(QtCore.QSize(20, 20))
        self.undoButton.setObjectName("undoButton")
        self.horizontalLayout.addWidget(self.undoButton)
        self.redoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/001-redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon2)
        self.redoButton.setIconSize(QtCore.QSize(20, 20))
        self.redoButton.setObjectName("redoButton")
        self.horizontalLayout.addWidget(self.redoButton)
        self.stepButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stepButton.setIcon(icon3)
        self.stepButton.setIconSize(QtCore.QSize(20, 20))
        self.stepButton.setObjectName("stepButton")
        self.horizontalLayout.addWidget(self.stepButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(1330, 130, 111, 28))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Resources/diagonal-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetButton.setIcon(icon4)
        self.resetButton.setIconSize(QtCore.QSize(20, 20))
        self.resetButton.setObjectName("resetButton")
        Coursework.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Coursework)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1639, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Coursework.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Coursework)
        self.statusbar.setObjectName("statusbar")
        Coursework.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Coursework)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(Coursework)
        self.actionExit.setObjectName("actionExit")
        self.actionSolve = QtWidgets.QAction(Coursework)
        self.actionSolve.setObjectName("actionSolve")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Coursework)
        QtCore.QMetaObject.connectSlotsByName(Coursework)

    def retranslateUi(self, Coursework):
        _translate = QtCore.QCoreApplication.translate
        Coursework.setWindowTitle(_translate("Coursework", "AI Coursework"))
        self.solveButton.setText(_translate("Coursework", "Solve"))
        self.algorithmsComboBox.setItemText(0, _translate("Coursework", "Djkstra"))
        self.twoWayCheckBox.setText(_translate("Coursework", "Two Way"))
        self.Loglabel.setText(_translate("Coursework", "Activity Log:"))
        self.distanceLabel.setText(_translate("Coursework", "Total Distance:"))
        self.undoButton.setToolTip(_translate("Coursework", "Undo"))
        self.undoButton.setText(_translate("Coursework", "Undo"))
        self.redoButton.setToolTip(_translate("Coursework", "Redo"))
        self.redoButton.setText(_translate("Coursework", "Redo"))
        self.stepButton.setToolTip(_translate("Coursework", "Step through"))
        self.stepButton.setText(_translate("Coursework", "Step"))
        self.resetButton.setToolTip(_translate("Coursework", "Step through"))
        self.resetButton.setText(_translate("Coursework", "  Reset"))
        self.menuFile.setTitle(_translate("Coursework", "File"))
        self.actionOpen.setText(_translate("Coursework", "Open"))
        self.actionExit.setText(_translate("Coursework", "Exit"))
        self.actionSolve.setText(_translate("Coursework", "Solve!"))

