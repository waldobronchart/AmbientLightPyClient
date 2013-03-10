import ui
from logger import log
from PyQt4 import QtGui, QtCore

class StatusBar(QtGui.QFrame):
    def __init__(self, *args):
        super(StatusBar, self).__init__(*args)
        log.info("Initializing StatusBar")
        
        self.ui = ui.Ui_StatusBar()
        self.handle = self.ui.setupUi(self)

        # Set drop shadow WarningsLabel
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(0)
        dropShadowEffect.setColor(QtGui.QColor("#343434"))
        dropShadowEffect.setOffset(0,1)
        self.ui.warningsLabel.setGraphicsEffect(dropShadowEffect)

        # Set drop shadow on StatusLabel
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(0)
        dropShadowEffect.setColor(QtGui.QColor("#343434"))
        dropShadowEffect.setOffset(0,1)
        self.ui.statusLabel.setGraphicsEffect(dropShadowEffect)
