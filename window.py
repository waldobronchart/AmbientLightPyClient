__author__ = 'Waldo'

from PyQt4 import QtGui, QtCore
import ui
from widget_titlebar import TitleBar
from widget_statusbar import StatusBar
from widget_sampler import Sampler
from logger import log

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

        # Add sampler widget
        self.ui.sampler = Sampler(self.ui.contentFrame)

        # Add titlebar yo
        self.ui.titlebar = TitleBar(self.ui.contentFrame)
        self.ui.titlebar.setMinimumWidth(contentWidth)

        # Titlebar button callbacks
        self.connect(self.ui.titlebar.samplerButton, QtCore.SIGNAL('toggled(bool)'), self.on_samplerButton_toggled)
        self.connect(self.ui.titlebar.colorsButton, QtCore.SIGNAL('toggled(bool)'), self.on_colorsButton_toggled)
        self.connect(self.ui.titlebar.serverButton, QtCore.SIGNAL('toggled(bool)'), self.on_serverButton_toggled)

        # Add statusbar
        self.ui.statusbar = StatusBar(self.ui.contentFrame)
        self.ui.statusbar.setMinimumWidth(contentWidth)
        self.ui.statusbar.move(0, contentHeight - self.ui.statusbar.height())

        # Positioning
        self.ui.sampler.move(0, self.ui.titlebar.height()-6)

    def on_samplerButton_toggled(self, checked):
        if checked:
            log.debug("Sampler button selected")
            self.ui.sampler.show()
        else:
            self.ui.sampler.hide()

    def on_colorsButton_toggled(self, checked):
        if checked:
            log.debug("Colors button selected")

    def on_serverButton_toggled(self, checked):
        if checked:
            log.debug("Server button selected")



## Show the main window
def show():
    instance = MainWindow.Instance
    if instance is None:
        instance = MainWindow()
    instance.show()