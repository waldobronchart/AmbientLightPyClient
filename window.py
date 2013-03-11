__author__ = 'Waldo'

from PyQt4 import QtGui, QtCore
import ui
from widget_sampler import Sampler
from logger import log



# todo: checkbox style
# todo: button style
# todo: server tab
# todo: write a statusbar logger
# todo: make window shadow transparent to events
class MainWindow(QtGui.QMainWindow):
    Instance = None

    def __init__(self):
        super(MainWindow, self).__init__()
        MainWindow.Instance = self
        self.titleBarClicked = False

        # Setup
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.ui = ui.Ui_MainWindow()
        self.window_handle = self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(1)

        # Setup drop shadow effects
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(20)
        dropShadowEffect.setColor(QtGui.QColor("#000000"))
        dropShadowEffect.setOffset(0,0)
        self.ui.shadowPadding.setGraphicsEffect(dropShadowEffect)
        self.addDropShadowToText(self.ui.titleLabel)
        self.addDropShadowToText(self.ui.statusBarWarningLabel)
        self.addDropShadowToText(self.ui.statusLabel)

        # The Sampler widget (this allows for selection of the tv sample bounds)
        self.ui.sampler = Sampler(self.ui.samplerTab)

    def addDropShadowToText(self, label):
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(0)
        dropShadowEffect.setColor(QtGui.QColor("#343434"))
        dropShadowEffect.setOffset(0,1)
        label.setGraphicsEffect(dropShadowEffect)

    def mousePressEvent(self, e):
        # Is mouse over the titlebar?
        titleBarPosInWindow = self.ui.titleBar.mapTo(self, self.ui.titleBar.pos())
        if self.ui.titleBar.rect().contains(e.pos() - titleBarPosInWindow):
            self.titleBarClicked = (e.button() == QtCore.Qt.LeftButton)
            if self.titleBarClicked:
                self.titleBarMoveMouseStart = e.globalPos() - self.pos()

    def mouseMoveEvent(self, e):
        if self.titleBarClicked:
            self.move(e.globalPos() - self.titleBarMoveMouseStart)

    def mouseReleaseEvent(self, e):
        if self.titleBarClicked and e.button() == QtCore.Qt.LeftButton:
            self.titleBarClicked = False

    def on_tabWidget_currentChanged(self, index):
        if isinstance(index, int):
            # Shamelessly position the arrow over the currently selected tab
            arrowOffset = QtCore.QPoint(198, 22)
            tabRect = self.ui.tabWidget.tabBar().tabRect(index)
            self.ui.tabSelectionArrow.move(tabRect.center() + arrowOffset)


## Show the main window
def show():
    instance = MainWindow.Instance
    if instance is None:
        instance = MainWindow()
    instance.show()