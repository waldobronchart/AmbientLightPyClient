# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titlebar.ui'
#
# Created: Sun Mar 10 10:26:24 2013
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
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 rgba(190, 190, 190, 255), \n"
"        stop:0.021739130 rgba(91, 91, 91, 255), \n"
"        stop:0.46 rgba(86, 86, 86, 255), \n"
"        stop:0.869565217 rgba(70, 70, 70, 255), \n"
"        stop:0.879565217 rgba(0, 0, 0, 128), \n"
"        stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"#titleLabel {\n"
"    font-family: Arial, sans-serif;\n"
"    color: #e4e4e4;\n"
"    margin-left: 16px;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"#closeButtonContainer {\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 128);\n"
"    border-top: 0;\n"
"}\n"
"\n"
"#closeButton {\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(172, 19, 19, 255), stop:1 rgba(141, 15, 15, 255));\n"
"    border: 1px solid #b03333;\n"
"    border-top: 1px solid #d13737;\n"
"}\n"
"\n"
"#closeButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #fc3838, stop:1 #cf2e2e);\n"
"    border: 1px solid #ff5b5b;\n"
"    border-top: 1px solid #ff8484;\n"
"}\n"
"\n"
"#closeButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #481515, stop:1 #5f1b1b);\n"
"    border: 1px solid #713a3a;\n"
"    border-top: 1px solid #813d3d;\n"
"}"))
        TitleBar.setFrameShape(QtGui.QFrame.StyledPanel)
        TitleBar.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(TitleBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.titleLabelContainer = QtGui.QVBoxLayout()
        self.titleLabelContainer.setSpacing(0)
        self.titleLabelContainer.setObjectName(_fromUtf8("titleLabelContainer"))
        self.titleLabel = QtGui.QLabel(TitleBar)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.titleLabelContainer.addWidget(self.titleLabel)
        spacerItem = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.titleLabelContainer.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.titleLabelContainer)
        spacerItem1 = QtGui.QSpacerItem(200, 13, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.buttonsVerticalContainer = QtGui.QVBoxLayout()
        self.buttonsVerticalContainer.setSpacing(0)
        self.buttonsVerticalContainer.setObjectName(_fromUtf8("buttonsVerticalContainer"))
        spacerItem2 = QtGui.QSpacerItem(20, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.buttonsVerticalContainer.addItem(spacerItem2)
        self.buttonsContainer = QtGui.QHBoxLayout()
        self.buttonsContainer.setSpacing(10)
        self.buttonsContainer.setObjectName(_fromUtf8("buttonsContainer"))
        self.buttonsVerticalContainer.addLayout(self.buttonsContainer)
        self.horizontalLayout_2.addLayout(self.buttonsVerticalContainer)
        spacerItem3 = QtGui.QSpacerItem(200, 13, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.windowButtonsContainer = QtGui.QVBoxLayout()
        self.windowButtonsContainer.setSpacing(0)
        self.windowButtonsContainer.setContentsMargins(-1, 0, -1, -1)
        self.windowButtonsContainer.setObjectName(_fromUtf8("windowButtonsContainer"))
        self.closeButtonContainer = QtGui.QFrame(TitleBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButtonContainer.sizePolicy().hasHeightForWidth())
        self.closeButtonContainer.setSizePolicy(sizePolicy)
        self.closeButtonContainer.setMinimumSize(QtCore.QSize(50, 23))
        self.closeButtonContainer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.closeButtonContainer.setFrameShadow(QtGui.QFrame.Raised)
        self.closeButtonContainer.setLineWidth(0)
        self.closeButtonContainer.setObjectName(_fromUtf8("closeButtonContainer"))
        self.closeButton = QtGui.QPushButton(self.closeButtonContainer)
        self.closeButton.setGeometry(QtCore.QRect(1, 0, 48, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(48, 22))
        self.closeButton.setMaximumSize(QtCore.QSize(22, 16777215))
        self.closeButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(20, 20))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.windowButtonsContainer.addWidget(self.closeButtonContainer)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.windowButtonsContainer.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.windowButtonsContainer)
        spacerItem5 = QtGui.QSpacerItem(12, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)

        self.retranslateUi(TitleBar)
        QtCore.QMetaObject.connectSlotsByName(TitleBar)

    def retranslateUi(self, TitleBar):
        TitleBar.setWindowTitle(_translate("TitleBar", "Frame", None))
        self.titleLabel.setText(_translate("TitleBar", "Ambient Light Settings", None))

import ui.titlebar_rc
