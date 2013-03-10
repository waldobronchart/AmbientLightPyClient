import ui
from logger import log
from PyQt4 import QtGui, QtCore

class TitleBarButton(QtGui.QFrame):
    def __init__(self, text, iconFile, *args):
        log.info("...creating a TitleBarButton: " + text)

        super(TitleBarButton, self).__init__(*args)
        self.ui = ui.Ui_TitleBarButton()
        self.handle = self.ui.setupUi(self)

        # Text
        self.ui.button.setText(" " + text.upper())

        # Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/resources/" + iconFile), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.button.setIcon(icon)

        # Set sizes
        self.ui.button.adjustSize()
        buttonWidth = self.ui.button.width()+14
        self.ui.button.setFixedWidth(buttonWidth)
        self.setFixedWidth(buttonWidth+2)

        # Align arrow
        self.ui.selectionArrow.move(buttonWidth/2-10, 24)
        self.ui.selectionArrow.hide()

    def on_button_toggled(self, checked):
        if checked:
            self.ui.selectionArrow.show()
        else:
            self.ui.selectionArrow.hide()