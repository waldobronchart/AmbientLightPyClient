# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titlebarbutton.ui'
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

class Ui_TitleBarButton(object):
    def setupUi(self, TitleBarButton):
        TitleBarButton.setObjectName(_fromUtf8("TitleBarButton"))
        TitleBarButton.resize(94, 34)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TitleBarButton.sizePolicy().hasHeightForWidth())
        TitleBarButton.setSizePolicy(sizePolicy)
        TitleBarButton.setMinimumSize(QtCore.QSize(50, 34))
        TitleBarButton.setMaximumSize(QtCore.QSize(16777215, 34))
        TitleBarButton.setStyleSheet(_fromUtf8("#TitleBarButton {\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 rgba(0, 0, 0, 50), \n"
"        stop:0.82352 rgba(0, 0, 0, 50), \n"
"        stop:0.82452 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"#button {\n"
"    font-size: 8pt;\n"
"    color: #ffffff;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 #575757,\n"
"        stop:0.892045 #484848,\n"
"        stop:1 #474747);\n"
"    border: 1px solid #5b5b5b;\n"
"    border-top: 1px solid #606060;\n"
"    border-bottom: 1px solid #505050;\n"
"}\n"
"\n"
"#button:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 #5b5b5b,\n"
"        stop:0.892045 #535353,\n"
"        stop:1 #4d4d4d);\n"
"    border: 1px solid #636363;\n"
"    border-top: 1px solid #747474;\n"
"}\n"
"\n"
"#button:pressed, #button:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 #1379ae,\n"
"        stop:0.892045 #116998, \n"
"        stop:1 #0f608e);\n"
"    border: 1px solid #1581b1;\n"
"    border-top: 1px solid #199cc4;\n"
"    border-bottom: 1px solid #10699a;\n"
"}"))
        self.button = QtGui.QPushButton(TitleBarButton)
        self.button.setGeometry(QtCore.QRect(1, 1, 90, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setMinimumSize(QtCore.QSize(0, 27))
        self.button.setMaximumSize(QtCore.QSize(16777215, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_sampler.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QtCore.QSize(16, 18))
        self.button.setCheckable(True)
        self.button.setChecked(False)
        self.button.setAutoExclusive(True)
        self.button.setFlat(False)
        self.button.setObjectName(_fromUtf8("button"))
        self.selectionArrow = QtGui.QLabel(TitleBarButton)
        self.selectionArrow.setGeometry(QtCore.QRect(40, 24, 20, 10))
        self.selectionArrow.setText(_fromUtf8(""))
        self.selectionArrow.setPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/button_selection_arrow.png")))
        self.selectionArrow.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.selectionArrow.setObjectName(_fromUtf8("selectionArrow"))

        self.retranslateUi(TitleBarButton)
        QtCore.QMetaObject.connectSlotsByName(TitleBarButton)

    def retranslateUi(self, TitleBarButton):
        TitleBarButton.setWindowTitle(_translate("TitleBarButton", "Form", None))
        self.button.setText(_translate("TitleBarButton", " SAMPLER", None))

import ui.titlebarbutton_rc
