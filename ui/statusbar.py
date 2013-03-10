# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusbar.ui'
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

class Ui_StatusBar(object):
    def setupUi(self, StatusBar):
        StatusBar.setObjectName(_fromUtf8("StatusBar"))
        StatusBar.resize(500, 31)
        StatusBar.setMaximumSize(QtCore.QSize(16777215, 31))
        StatusBar.setMouseTracking(False)
        StatusBar.setStyleSheet(_fromUtf8("#StatusBar {\n"
"    border-bottom-left-radius: 9px;\n"
"    border-bottom-right-radius: 9px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 rgba(0, 0, 0, 0),\n"
"        stop:0.193548387 rgba(0, 0, 0, 90), \n"
"        stop:0.194548387 rgba(190, 190, 190, 255), \n"
"        stop:0.225806451 rgba(91, 91, 91, 255), \n"
"        stop:0.580645161 rgba(86, 86, 86, 255), \n"
"        stop:1 rgba(70, 70, 70, 255));\n"
"}\n"
"\n"
"#warningsLabel, #statusLabel {\n"
"    font-family: Arial, sans-serif;\n"
"    color: #e4e4e4;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"#divider {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
"        stop:0 rgba(255, 255, 255, 30), \n"
"        stop:0.49 rgba(255, 255, 255, 30), \n"
"        stop:0.5 rgba(0, 0, 0, 43));\n"
"}"))
        StatusBar.setFrameShape(QtGui.QFrame.StyledPanel)
        StatusBar.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(StatusBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.contentContainer = QtGui.QVBoxLayout()
        self.contentContainer.setSpacing(0)
        self.contentContainer.setObjectName(_fromUtf8("contentContainer"))
        spacerItem = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.contentContainer.addItem(spacerItem)
        self.contentHorizontalLayout = QtGui.QHBoxLayout()
        self.contentHorizontalLayout.setSpacing(12)
        self.contentHorizontalLayout.setObjectName(_fromUtf8("contentHorizontalLayout"))
        self.warningsContainer = QtGui.QHBoxLayout()
        self.warningsContainer.setSpacing(3)
        self.warningsContainer.setContentsMargins(10, -1, -1, -1)
        self.warningsContainer.setObjectName(_fromUtf8("warningsContainer"))
        self.warningsIcon = QtGui.QLabel(StatusBar)
        self.warningsIcon.setMinimumSize(QtCore.QSize(20, 20))
        self.warningsIcon.setText(_fromUtf8(""))
        self.warningsIcon.setTextFormat(QtCore.Qt.PlainText)
        self.warningsIcon.setPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_warning.png")))
        self.warningsIcon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.warningsIcon.setMargin(-1)
        self.warningsIcon.setIndent(0)
        self.warningsIcon.setObjectName(_fromUtf8("warningsIcon"))
        self.warningsContainer.addWidget(self.warningsIcon)
        self.warningsLabel = QtGui.QLabel(StatusBar)
        self.warningsLabel.setObjectName(_fromUtf8("warningsLabel"))
        self.warningsContainer.addWidget(self.warningsLabel)
        spacerItem1 = QtGui.QSpacerItem(9, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.warningsContainer.addItem(spacerItem1)
        self.divider = QtGui.QFrame(StatusBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divider.sizePolicy().hasHeightForWidth())
        self.divider.setSizePolicy(sizePolicy)
        self.divider.setMinimumSize(QtCore.QSize(2, 25))
        self.divider.setMaximumSize(QtCore.QSize(2, 25))
        self.divider.setStyleSheet(_fromUtf8(""))
        self.divider.setFrameShape(QtGui.QFrame.StyledPanel)
        self.divider.setFrameShadow(QtGui.QFrame.Raised)
        self.divider.setLineWidth(0)
        self.divider.setObjectName(_fromUtf8("divider"))
        self.warningsContainer.addWidget(self.divider)
        self.contentHorizontalLayout.addLayout(self.warningsContainer)
        self.statusLabel = QtGui.QLabel(StatusBar)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.contentHorizontalLayout.addWidget(self.statusLabel)
        self.contentContainer.addLayout(self.contentHorizontalLayout)
        self.horizontalLayout.addLayout(self.contentContainer)
        spacerItem2 = QtGui.QSpacerItem(177, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.retranslateUi(StatusBar)
        QtCore.QMetaObject.connectSlotsByName(StatusBar)

    def retranslateUi(self, StatusBar):
        StatusBar.setWindowTitle(_translate("StatusBar", "Frame", None))
        self.warningsLabel.setText(_translate("StatusBar", "33", None))
        self.statusLabel.setText(_translate("StatusBar", "Connected to server (192.168.1.70:31337)", None))

import ui.statusbar_rc
