# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(660, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(660, 600))
        MainWindow.setStyleSheet(_fromUtf8("#MainWindow {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}"))
        MainWindow.setAnimated(True)
        self.CentralWidget = QtGui.QWidget(MainWindow)
        self.CentralWidget.setStyleSheet(_fromUtf8("#centralWidget { background-color: #ffffff; }    "))
        self.CentralWidget.setObjectName(_fromUtf8("CentralWidget"))
        self.centralWidget = QtGui.QVBoxLayout(self.CentralWidget)
        self.centralWidget.setSpacing(0)
        self.centralWidget.setMargin(20)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.InnerLayout = QtGui.QVBoxLayout()
        self.InnerLayout.setSpacing(0)
        self.InnerLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.InnerLayout.setObjectName(_fromUtf8("InnerLayout"))
        self.centralWidget.addLayout(self.InnerLayout)
        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

