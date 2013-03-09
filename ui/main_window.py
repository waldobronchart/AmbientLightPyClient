# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat Mar  9 22:08:20 2013
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
        MainWindow.resize(680, 585)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(680, 585))
        MainWindow.setStyleSheet(_fromUtf8("#contentFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 rgba(53, 58, 62, 0), \n"
"    stop:0.05 rgba(53, 58, 62, 0), \n"
"    stop:0.051 rgba(53, 58, 62, 255), \n"
"    stop:0.96 rgba(53, 58, 62, 255), \n"
"    stop:0.961 rgba(53, 58, 62, 0), \n"
"    stop:1 rgba(53, 58, 62, 0));\n"
"}"))
        MainWindow.setAnimated(True)
        self.shadowPadding = QtGui.QWidget(MainWindow)
        self.shadowPadding.setStyleSheet(_fromUtf8("#centralWidget { background-color: #ffffff; }    "))
        self.shadowPadding.setObjectName(_fromUtf8("shadowPadding"))
        self.shadowPad = QtGui.QVBoxLayout(self.shadowPadding)
        self.shadowPad.setSpacing(0)
        self.shadowPad.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.shadowPad.setMargin(20)
        self.shadowPad.setObjectName(_fromUtf8("shadowPad"))
        self.contentFrame = QtGui.QFrame(self.shadowPadding)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy)
        self.contentFrame.setMinimumSize(QtCore.QSize(640, 545))
        self.contentFrame.setMaximumSize(QtCore.QSize(640, 545))
        self.contentFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.contentFrame.setLineWidth(0)
        self.contentFrame.setObjectName(_fromUtf8("contentFrame"))
        self.shadowPad.addWidget(self.contentFrame)
        MainWindow.setCentralWidget(self.shadowPadding)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

