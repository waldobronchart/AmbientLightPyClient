__author__ = 'Waldo'

from PyQt4 import QtGui, QtCore
import ui
from widget_titlebar import TitleBar

class MainWindow(QtGui.QMainWindow):
    Instance = None

    def __init__(self):
        super(MainWindow, self).__init__()
        MainWindow.Instance = self

        # Setup
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.ui = ui.Ui_MainWindow()
        self.window_handle = self.ui.setupUi(self)

        # Setup drop shadow effect
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(10)
        dropShadowEffect.setColor(QtGui.QColor("#000000"))
        dropShadowEffect.setOffset(0,0)
        self.ui.CentralWidget.setGraphicsEffect(dropShadowEffect)

        # Add toolbar yo
        self.ui.titlebar = TitleBar()
        self.ui.InnerLayout.addWidget(self.ui.titlebar)



## Show the main window
def show():
    instance = MainWindow.Instance
    if instance is None:
        instance = MainWindow()
    instance.show()