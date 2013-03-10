__author__ = 'Waldo'

import ui
from logger import log
from PyQt4 import QtGui, QtCore
from widget_titlebar_button import TitleBarButton

class TitleBar(QtGui.QFrame):
    def __init__(self, *args):
        log.info("Initializing TitleBar")
        super(TitleBar, self).__init__(*args)
        self.ui = ui.Ui_TitleBar()
        self.handle = self.ui.setupUi(self)
        self.toolbarClicked = False

        # Set drop shadow on title text
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(0)
        dropShadowEffect.setColor(QtGui.QColor("#343434"))
        dropShadowEffect.setOffset(0,1)
        self.ui.titleLabel.setGraphicsEffect(dropShadowEffect)

        # Add buttons to titlebar
        self.ui.buttonGroup = QtGui.QButtonGroup(self)
        self.samplerButton = self.addButton("SAMPLER", "icon_sampler.png").ui.button
        self.colorsButton = self.addButton("COLORS", "icon_colors.png").ui.button
        self.serverButton = self.addButton("SERVER", "icon_server.png").ui.button

        # Select sampler button by default
        self.samplerButton.setChecked(True)

    def addButton(self, text, icon):
        button = TitleBarButton(text, icon)
        self.ui.buttonsContainer.addWidget(button)
        self.ui.buttonGroup.addButton(button.ui.button)
        return button

    def on_closeButton_clicked(self, *args):
        if not args:
            self.window().close()

    def on_minimizeButton_clicked(self, *args):
        if not args:
            self.window().setWindowState(QtCore.Qt.WindowMinimized)

    def mousePressEvent(self, e):
        self.toolbarClicked = (e.button() == QtCore.Qt.LeftButton)
        if self.toolbarClicked:
            posInWindow = self.mapTo(self.window(), self.pos())
            self.tbMouseStart = (e.x() + posInWindow.x(), e.y() + posInWindow.x())

    def mouseReleaseEvent(self, e):
        if self.toolbarClicked and e.button() == QtCore.Qt.LeftButton:
            self.toolbarClicked = False

    def mouseMoveEvent(self, e):
        if self.toolbarClicked:
            self.window().move(e.globalX() - self.tbMouseStart[0], e.globalY() - self.tbMouseStart[1])