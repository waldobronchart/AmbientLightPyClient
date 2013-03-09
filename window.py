__author__ = 'Waldo'

from PyQt4 import QtGui, QtCore
import ui
from widget_titlebar import TitleBar
from widget_statusbar import StatusBar

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
        dropShadowEffect.setBlurRadius(20)
        dropShadowEffect.setColor(QtGui.QColor("#000000"))
        dropShadowEffect.setOffset(0,0)
        self.ui.shadowPadding.setGraphicsEffect(dropShadowEffect)

        # Inner frame content
        contentRect = self.ui.contentFrame.frameRect()
        contentWidth = contentRect.width()
        contentHeight = contentRect.height()

        # Add toolbar yo
        self.ui.titlebar = TitleBar(self.ui.contentFrame)
        self.ui.titlebar.setMinimumWidth(contentWidth)
        #self.ui.titlebar.
        #self.ui.InnerLayout.addWidget(self.ui.titlebar)

        # Add statusbar
        self.ui.statusbar = StatusBar(self.ui.contentFrame)
        self.ui.statusbar.setMinimumWidth(contentWidth)
        self.ui.statusbar.move(0, contentHeight - self.ui.statusbar.height())



## Show the main window
def show():
    instance = MainWindow.Instance
    if instance is None:
        instance = MainWindow()
    instance.show()