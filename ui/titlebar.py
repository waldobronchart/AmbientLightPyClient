# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titlebar.ui'
#
# Created: Sat Mar  9 19:25:36 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TitleBar(object):
    def setupUi(self, TitleBar):
        TitleBar.setObjectName(_fromUtf8("TitleBar"))
        TitleBar.resize(500, 46)
        TitleBar.setMaximumSize(QtCore.QSize(16777215, 46))
        TitleBar.setMouseTracking(False)
        TitleBar.setStyleSheet(_fromUtf8("#TitleBar {\n"
"    border-top-left-radius: 9px;\n"
"    border-top-right-radius: 9px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.021739130 rgba(91, 91, 91, 255), stop:0.869565217 rgba(70, 70, 70, 255), stop:0.879565217 rgba(0, 0, 0, 200), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"#TitleLabel {\n"
"    font-family: Arial, sans-serif;\n"
"    color: #e4e4e4;\n"
"    margin-left: 16px;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"#CloseButtonContainer {\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 128);\n"
"    border-top: 0;\n"
"}\n"
"\n"
"#CloseButton {\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(172, 19, 19, 255), stop:1 rgba(141, 15, 15, 255));\n"
"    border: 1px solid #b03333;\n"
"    border-top: 1px solid #d13737;\n"
"}\n"
"\n"
"#CloseButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #fc3838, stop:1 #cf2e2e);\n"
"    border: 1px solid #ff5b5b;\n"
"    border-top: 1px solid #ff8484;\n"
"}\n"
"\n"
"#CloseButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #481515, stop:1 #5f1b1b);\n"
"    border: 1px solid #713a3a;\n"
"    border-top: 1px solid #813d3d;\n"
"}"))
        TitleBar.setFrameShape(QtGui.QFrame.StyledPanel)
        TitleBar.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(TitleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.TitleLabelContainer = QtGui.QVBoxLayout()
        self.TitleLabelContainer.setSpacing(0)
        self.TitleLabelContainer.setObjectName(_fromUtf8("TitleLabelContainer"))
        self.TitleLabel = QtGui.QLabel(TitleBar)
        self.TitleLabel.setObjectName(_fromUtf8("TitleLabel"))
        self.TitleLabelContainer.addWidget(self.TitleLabel)
        spacerItem = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.TitleLabelContainer.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.TitleLabelContainer)
        spacerItem1 = QtGui.QSpacerItem(439, 13, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ButtonsContainer = QtGui.QVBoxLayout()
        self.ButtonsContainer.setSpacing(0)
        self.ButtonsContainer.setContentsMargins(-1, 0, -1, -1)
        self.ButtonsContainer.setObjectName(_fromUtf8("ButtonsContainer"))
        self.CloseButtonContainer = QtGui.QFrame(TitleBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButtonContainer.sizePolicy().hasHeightForWidth())
        self.CloseButtonContainer.setSizePolicy(sizePolicy)
        self.CloseButtonContainer.setMinimumSize(QtCore.QSize(50, 23))
        self.CloseButtonContainer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.CloseButtonContainer.setFrameShadow(QtGui.QFrame.Raised)
        self.CloseButtonContainer.setLineWidth(0)
        self.CloseButtonContainer.setObjectName(_fromUtf8("CloseButtonContainer"))
        self.CloseButton = QtGui.QPushButton(self.CloseButtonContainer)
        self.CloseButton.setGeometry(QtCore.QRect(1, 0, 48, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setMinimumSize(QtCore.QSize(48, 22))
        self.CloseButton.setMaximumSize(QtCore.QSize(22, 16777215))
        self.CloseButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/icon_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseButton.setIcon(icon)
        self.CloseButton.setIconSize(QtCore.QSize(20, 20))
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.ButtonsContainer.addWidget(self.CloseButtonContainer)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.ButtonsContainer.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.ButtonsContainer)
        spacerItem3 = QtGui.QSpacerItem(12, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.retranslateUi(TitleBar)
        QtCore.QMetaObject.connectSlotsByName(TitleBar)

    def retranslateUi(self, TitleBar):
        TitleBar.setWindowTitle(_translate("TitleBar", "Frame", None))
        self.TitleLabel.setText(_translate("TitleBar", "Ambient Light Settings", None))

import ui.resources_rc
