# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed Mar 13 00:00:43 2013
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
        MainWindow.setStyleSheet(_fromUtf8("QLabel {\n"
"    font-family: Arial, sans-serif;\n"
"    color: #e4e4e4;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"#contentFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 rgba(53, 58, 62, 0), \n"
"    stop:0.05 rgba(53, 58, 62, 0), \n"
"    stop:0.051 rgba(53, 58, 62, 255), \n"
"    stop:0.96 rgba(53, 58, 62, 255), \n"
"    stop:0.961 rgba(53, 58, 62, 0), \n"
"    stop:1 rgba(53, 58, 62, 0));\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(:ui/resources/slider_bg.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"    margin: 0 3px 0 3px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    border-image: url(:ui/resources/slider_bg_fill.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"    margin: 1px 0 2px 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(:ui/resources/slider_handle.png);\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    margin: -2px -14px -4px -9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-image: url(:ui/resources/slider_handle_hover.png);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(:ui/resources/slider_handle_pressed.png);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QCheckBox {\n"
"    margin-top: 1px;\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 18px;\n"
"     height: 18px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"     image: url(:ui/resources/checkbox_unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:hover {\n"
"     image: url(:ui/resources/checkbox_unchecked_hover.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:pressed {\n"
"     image: url(:ui/resources/checkbox_checked_pressed.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"     image: url(:ui/resources/checkbox_checked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"     image: url(:ui/resources/checkbox_checked_hover.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"     image: url(:ui/resources/checkbox_checked_pressed.png);\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""))
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
        self.titleBar = QtGui.QFrame(self.contentFrame)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 640, 40))
        self.titleBar.setStyleSheet(_fromUtf8("#titleBar {\n"
"    border-image: url(:ui/resources/titlebar_bg.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"}"))
        self.titleBar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QtGui.QFrame.Raised)
        self.titleBar.setObjectName(_fromUtf8("titleBar"))
        self.titleLabel = QtGui.QLabel(self.titleBar)
        self.titleLabel.setGeometry(QtCore.QRect(20, 13, 131, 16))
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.tabWidget = QtGui.QTabWidget(self.contentFrame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 12, 640, 508))
        self.tabWidget.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 0px;\n"
"}\n"
" \n"
"QTabWidget::tab-bar  {\n"
"    left: 212px;\n"
"}\n"
" \n"
"QTabBar::tab  {\n"
"    font-size: 8pt;\n"
"    color: #ffffff;\n"
"    border-image: url(:ui/resources/titlebar_button_bg.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"    margin-right: 10px;\n"
"    padding: 1px 0 0 3px;\n"
"    height: 27px;\n"
"}\n"
" \n"
"QTabBar::tab:hover  {\n"
"    border-image: url(:ui/resources/titlebar_button_bg_hover.png) 0 8 0 8;\n"
"}\n"
" \n"
"QTabBar::tab:selected  {\n"
"    border-image: url(:ui/resources/titlebar_button_bg_selected.png) 0 8 0 8;\n"
"}"))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 18))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.samplerTab = QtGui.QWidget()
        self.samplerTab.setObjectName(_fromUtf8("samplerTab"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_sampler.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.samplerTab, icon, _fromUtf8(""))
        self.colorsTab = QtGui.QWidget()
        self.colorsTab.setStyleSheet(_fromUtf8("#colorsTab QLabel {\n"
"    font-size: 8pt;\n"
"}"))
        self.colorsTab.setObjectName(_fromUtf8("colorsTab"))
        self.widget = QtGui.QWidget(self.colorsTab)
        self.widget.setGeometry(QtCore.QRect(190, 1, 258, 481))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.colorsTabLayout = QtGui.QVBoxLayout(self.widget)
        self.colorsTabLayout.setSpacing(10)
        self.colorsTabLayout.setMargin(0)
        self.colorsTabLayout.setObjectName(_fromUtf8("colorsTabLayout"))
        spacerItem = QtGui.QSpacerItem(20, 70, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.colorsTabLayout.addItem(spacerItem)
        self.fadeDurationLayout = QtGui.QVBoxLayout()
        self.fadeDurationLayout.setSpacing(2)
        self.fadeDurationLayout.setObjectName(_fromUtf8("fadeDurationLayout"))
        self.fadeDurationLabel = QtGui.QLabel(self.widget)
        self.fadeDurationLabel.setMargin(0)
        self.fadeDurationLabel.setIndent(8)
        self.fadeDurationLabel.setObjectName(_fromUtf8("fadeDurationLabel"))
        self.fadeDurationLayout.addWidget(self.fadeDurationLabel)
        self.fadeDurationSlider = QtGui.QSlider(self.widget)
        self.fadeDurationSlider.setMaximum(1000)
        self.fadeDurationSlider.setSingleStep(1)
        self.fadeDurationSlider.setPageStep(10)
        self.fadeDurationSlider.setProperty("value", 200)
        self.fadeDurationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fadeDurationSlider.setTickInterval(10)
        self.fadeDurationSlider.setObjectName(_fromUtf8("fadeDurationSlider"))
        self.fadeDurationLayout.addWidget(self.fadeDurationSlider)
        self.colorsTabLayout.addLayout(self.fadeDurationLayout)
        self.colorHueLayout = QtGui.QVBoxLayout()
        self.colorHueLayout.setSpacing(2)
        self.colorHueLayout.setObjectName(_fromUtf8("colorHueLayout"))
        self.colorHueLabelLayout = QtGui.QHBoxLayout()
        self.colorHueLabelLayout.setObjectName(_fromUtf8("colorHueLabelLayout"))
        self.colorHueLabel = QtGui.QLabel(self.widget)
        self.colorHueLabel.setMargin(0)
        self.colorHueLabel.setIndent(8)
        self.colorHueLabel.setObjectName(_fromUtf8("colorHueLabel"))
        self.colorHueLabelLayout.addWidget(self.colorHueLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.colorHueLabelLayout.addItem(spacerItem1)
        self.colorHueCheckBox = QtGui.QCheckBox(self.widget)
        self.colorHueCheckBox.setText(_fromUtf8(""))
        self.colorHueCheckBox.setChecked(True)
        self.colorHueCheckBox.setObjectName(_fromUtf8("colorHueCheckBox"))
        self.colorHueLabelLayout.addWidget(self.colorHueCheckBox)
        self.colorHueLayout.addLayout(self.colorHueLabelLayout)
        self.colorHueSlider = QtGui.QSlider(self.widget)
        self.colorHueSlider.setStyleSheet(_fromUtf8("#colorHueSlider::groove:horizontal {\n"
"    border-image: url(:ui/resources/slider_bg_hue.png) 0 8 0 8;\n"
"}\n"
"\n"
"#colorHueSlider::sub-page:horizontal {\n"
"    border-image: none;\n"
"}"))
        self.colorHueSlider.setMaximum(1000)
        self.colorHueSlider.setProperty("value", 50)
        self.colorHueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.colorHueSlider.setObjectName(_fromUtf8("colorHueSlider"))
        self.colorHueLayout.addWidget(self.colorHueSlider)
        self.colorsTabLayout.addLayout(self.colorHueLayout)
        self.colorSaturationLayout = QtGui.QVBoxLayout()
        self.colorSaturationLayout.setSpacing(2)
        self.colorSaturationLayout.setObjectName(_fromUtf8("colorSaturationLayout"))
        self.colorSaturationLabel = QtGui.QLabel(self.widget)
        self.colorSaturationLabel.setEnabled(True)
        self.colorSaturationLabel.setMargin(0)
        self.colorSaturationLabel.setIndent(8)
        self.colorSaturationLabel.setObjectName(_fromUtf8("colorSaturationLabel"))
        self.colorSaturationLayout.addWidget(self.colorSaturationLabel)
        self.colorSaturationSlider = QtGui.QSlider(self.widget)
        self.colorSaturationSlider.setMaximum(255)
        self.colorSaturationSlider.setPageStep(10)
        self.colorSaturationSlider.setProperty("value", 200)
        self.colorSaturationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.colorSaturationSlider.setObjectName(_fromUtf8("colorSaturationSlider"))
        self.colorSaturationLayout.addWidget(self.colorSaturationSlider)
        self.colorsTabLayout.addLayout(self.colorSaturationLayout)
        self.colorBrightnessLayout = QtGui.QVBoxLayout()
        self.colorBrightnessLayout.setSpacing(2)
        self.colorBrightnessLayout.setObjectName(_fromUtf8("colorBrightnessLayout"))
        self.colorBrightnessLabel = QtGui.QLabel(self.widget)
        self.colorBrightnessLabel.setMargin(0)
        self.colorBrightnessLabel.setIndent(8)
        self.colorBrightnessLabel.setObjectName(_fromUtf8("colorBrightnessLabel"))
        self.colorBrightnessLayout.addWidget(self.colorBrightnessLabel)
        self.colorBrightnessSlider = QtGui.QSlider(self.widget)
        self.colorBrightnessSlider.setMinimum(-100)
        self.colorBrightnessSlider.setMaximum(100)
        self.colorBrightnessSlider.setPageStep(10)
        self.colorBrightnessSlider.setProperty("value", 0)
        self.colorBrightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.colorBrightnessSlider.setObjectName(_fromUtf8("colorBrightnessSlider"))
        self.colorBrightnessLayout.addWidget(self.colorBrightnessSlider)
        self.colorsTabLayout.addLayout(self.colorBrightnessLayout)
        self.camSaturationLayout = QtGui.QVBoxLayout()
        self.camSaturationLayout.setSpacing(2)
        self.camSaturationLayout.setObjectName(_fromUtf8("camSaturationLayout"))
        self.camSaturationLabel = QtGui.QLabel(self.widget)
        self.camSaturationLabel.setMargin(0)
        self.camSaturationLabel.setIndent(8)
        self.camSaturationLabel.setObjectName(_fromUtf8("camSaturationLabel"))
        self.camSaturationLayout.addWidget(self.camSaturationLabel)
        self.camSaturationSlider = QtGui.QSlider(self.widget)
        self.camSaturationSlider.setMaximum(255)
        self.camSaturationSlider.setPageStep(10)
        self.camSaturationSlider.setProperty("value", 74)
        self.camSaturationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.camSaturationSlider.setObjectName(_fromUtf8("camSaturationSlider"))
        self.camSaturationLayout.addWidget(self.camSaturationSlider)
        self.colorsTabLayout.addLayout(self.camSaturationLayout)
        self.camBrightnessLayout = QtGui.QVBoxLayout()
        self.camBrightnessLayout.setSpacing(2)
        self.camBrightnessLayout.setObjectName(_fromUtf8("camBrightnessLayout"))
        self.camBrightnessLabel = QtGui.QLabel(self.widget)
        self.camBrightnessLabel.setMargin(0)
        self.camBrightnessLabel.setIndent(8)
        self.camBrightnessLabel.setObjectName(_fromUtf8("camBrightnessLabel"))
        self.camBrightnessLayout.addWidget(self.camBrightnessLabel)
        self.camBrightnessSlider = QtGui.QSlider(self.widget)
        self.camBrightnessSlider.setMaximum(255)
        self.camBrightnessSlider.setPageStep(10)
        self.camBrightnessSlider.setProperty("value", 90)
        self.camBrightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.camBrightnessSlider.setObjectName(_fromUtf8("camBrightnessSlider"))
        self.camBrightnessLayout.addWidget(self.camBrightnessSlider)
        self.colorsTabLayout.addLayout(self.camBrightnessLayout)
        self.camContrastLayout = QtGui.QVBoxLayout()
        self.camContrastLayout.setSpacing(2)
        self.camContrastLayout.setObjectName(_fromUtf8("camContrastLayout"))
        self.camContrastLabel = QtGui.QLabel(self.widget)
        self.camContrastLabel.setMargin(0)
        self.camContrastLabel.setIndent(8)
        self.camContrastLabel.setObjectName(_fromUtf8("camContrastLabel"))
        self.camContrastLayout.addWidget(self.camContrastLabel)
        self.camContrastSlider = QtGui.QSlider(self.widget)
        self.camContrastSlider.setMaximum(255)
        self.camContrastSlider.setPageStep(10)
        self.camContrastSlider.setProperty("value", 20)
        self.camContrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.camContrastSlider.setObjectName(_fromUtf8("camContrastSlider"))
        self.camContrastLayout.addWidget(self.camContrastSlider)
        self.colorsTabLayout.addLayout(self.camContrastLayout)
        self.camGainLayout = QtGui.QVBoxLayout()
        self.camGainLayout.setSpacing(2)
        self.camGainLayout.setObjectName(_fromUtf8("camGainLayout"))
        self.camGainLabel = QtGui.QLabel(self.widget)
        self.camGainLabel.setMargin(0)
        self.camGainLabel.setIndent(8)
        self.camGainLabel.setObjectName(_fromUtf8("camGainLabel"))
        self.camGainLayout.addWidget(self.camGainLabel)
        self.camGainSlider = QtGui.QSlider(self.widget)
        self.camGainSlider.setMaximum(255)
        self.camGainSlider.setPageStep(10)
        self.camGainSlider.setProperty("value", 210)
        self.camGainSlider.setOrientation(QtCore.Qt.Horizontal)
        self.camGainSlider.setObjectName(_fromUtf8("camGainSlider"))
        self.camGainLayout.addWidget(self.camGainSlider)
        self.colorsTabLayout.addLayout(self.camGainLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.colorsTabLayout.addItem(spacerItem2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_colors.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.colorsTab, icon1, _fromUtf8(""))
        self.serverTab = QtGui.QWidget()
        self.serverTab.setObjectName(_fromUtf8("serverTab"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_server.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.serverTab, icon2, _fromUtf8(""))
        self.titleBarShadow = QtGui.QFrame(self.contentFrame)
        self.titleBarShadow.setGeometry(QtCore.QRect(-1, 39, 640, 8))
        self.titleBarShadow.setStyleSheet(_fromUtf8("#titleBarShadow {\n"
"    background: url(:ui/resources/titlebar_shadow.png);\n"
"    background-position: top;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}"))
        self.titleBarShadow.setFrameShape(QtGui.QFrame.StyledPanel)
        self.titleBarShadow.setFrameShadow(QtGui.QFrame.Raised)
        self.titleBarShadow.setLineWidth(0)
        self.titleBarShadow.setObjectName(_fromUtf8("titleBarShadow"))
        self.tabSelectionArrow = QtGui.QFrame(self.contentFrame)
        self.tabSelectionArrow.setGeometry(QtCore.QRect(352, 35, 20, 10))
        self.tabSelectionArrow.setStyleSheet(_fromUtf8("#tabSelectionArrow {\n"
"    width: 20px;\n"
"    height: 10px;\n"
"    background: url(:ui/resources/titlebar_button_arrow.png);\n"
"    background-position: top left;\n"
"}"))
        self.tabSelectionArrow.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tabSelectionArrow.setFrameShadow(QtGui.QFrame.Raised)
        self.tabSelectionArrow.setObjectName(_fromUtf8("tabSelectionArrow"))
        self.titleBarCloseButton = QtGui.QPushButton(self.contentFrame)
        self.titleBarCloseButton.setGeometry(QtCore.QRect(580, 0, 48, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBarCloseButton.sizePolicy().hasHeightForWidth())
        self.titleBarCloseButton.setSizePolicy(sizePolicy)
        self.titleBarCloseButton.setMinimumSize(QtCore.QSize(48, 22))
        self.titleBarCloseButton.setMaximumSize(QtCore.QSize(22, 22))
        self.titleBarCloseButton.setStyleSheet(_fromUtf8("#titleBarCloseButton {\n"
"    border-image: url(:ui/resources/titlebar_closebutton_bg.png) 0 6 0 6;\n"
"    border-left: 6px;\n"
"    border-right: 6px;\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"#titleBarCloseButton:hover {\n"
"    border-image: url(:ui/resources/titlebar_closebutton_bg_hover.png) 0 6 0 6;\n"
"}\n"
"\n"
"#titleBarCloseButton:pressed {\n"
"    border-image: url(:ui/resources/titlebar_closebutton_bg_pressed.png) 0 6 0 6;\n"
"}"))
        self.titleBarCloseButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.titleBarCloseButton.setIcon(icon3)
        self.titleBarCloseButton.setIconSize(QtCore.QSize(20, 20))
        self.titleBarCloseButton.setObjectName(_fromUtf8("titleBarCloseButton"))
        self.statusBar = QtGui.QFrame(self.contentFrame)
        self.statusBar.setGeometry(QtCore.QRect(0, 520, 640, 25))
        self.statusBar.setMinimumSize(QtCore.QSize(640, 25))
        self.statusBar.setMaximumSize(QtCore.QSize(640, 25))
        self.statusBar.setStyleSheet(_fromUtf8("#statusBar {\n"
"    border-image: url(:ui/resources/statusbar_bg.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"}"))
        self.statusBar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.statusBar.setFrameShadow(QtGui.QFrame.Raised)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.statusBar)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.statusBarWarningsContainer = QtGui.QHBoxLayout()
        self.statusBarWarningsContainer.setSpacing(3)
        self.statusBarWarningsContainer.setContentsMargins(0, -1, 6, -1)
        self.statusBarWarningsContainer.setObjectName(_fromUtf8("statusBarWarningsContainer"))
        self.statusBarWarningIcon = QtGui.QLabel(self.statusBar)
        self.statusBarWarningIcon.setMinimumSize(QtCore.QSize(20, 20))
        self.statusBarWarningIcon.setText(_fromUtf8(""))
        self.statusBarWarningIcon.setTextFormat(QtCore.Qt.PlainText)
        self.statusBarWarningIcon.setPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_warning.png")))
        self.statusBarWarningIcon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusBarWarningIcon.setMargin(0)
        self.statusBarWarningIcon.setIndent(0)
        self.statusBarWarningIcon.setObjectName(_fromUtf8("statusBarWarningIcon"))
        self.statusBarWarningsContainer.addWidget(self.statusBarWarningIcon)
        self.statusBarWarningLabel = QtGui.QLabel(self.statusBar)
        self.statusBarWarningLabel.setObjectName(_fromUtf8("statusBarWarningLabel"))
        self.statusBarWarningsContainer.addWidget(self.statusBarWarningLabel)
        spacerItem3 = QtGui.QSpacerItem(9, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.statusBarWarningsContainer.addItem(spacerItem3)
        self.statusBarWarningsDivider = QtGui.QFrame(self.statusBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBarWarningsDivider.sizePolicy().hasHeightForWidth())
        self.statusBarWarningsDivider.setSizePolicy(sizePolicy)
        self.statusBarWarningsDivider.setMinimumSize(QtCore.QSize(2, 25))
        self.statusBarWarningsDivider.setMaximumSize(QtCore.QSize(2, 25))
        self.statusBarWarningsDivider.setStyleSheet(_fromUtf8("#statusBarWarningsDivider {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
"        stop:0 rgba(255, 255, 255, 30), \n"
"        stop:0.49 rgba(255, 255, 255, 30), \n"
"        stop:0.5 rgba(0, 0, 0, 43));\n"
"}"))
        self.statusBarWarningsDivider.setFrameShape(QtGui.QFrame.StyledPanel)
        self.statusBarWarningsDivider.setFrameShadow(QtGui.QFrame.Raised)
        self.statusBarWarningsDivider.setLineWidth(0)
        self.statusBarWarningsDivider.setObjectName(_fromUtf8("statusBarWarningsDivider"))
        self.statusBarWarningsContainer.addWidget(self.statusBarWarningsDivider)
        self.horizontalLayout.addLayout(self.statusBarWarningsContainer)
        self.statusLabel = QtGui.QLabel(self.statusBar)
        self.statusLabel.setMargin(0)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout.addWidget(self.statusLabel)
        spacerItem4 = QtGui.QSpacerItem(322, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.statusBarShadow = QtGui.QFrame(self.contentFrame)
        self.statusBarShadow.setGeometry(QtCore.QRect(0, 513, 640, 8))
        self.statusBarShadow.setStyleSheet(_fromUtf8("#statusBarShadow {\n"
"    background: url(:ui/resources/statusbar_shadow.png);\n"
"    background-position: top;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}"))
        self.statusBarShadow.setFrameShape(QtGui.QFrame.StyledPanel)
        self.statusBarShadow.setFrameShadow(QtGui.QFrame.Raised)
        self.statusBarShadow.setLineWidth(0)
        self.statusBarShadow.setObjectName(_fromUtf8("statusBarShadow"))
        self.shadowPad.addWidget(self.contentFrame)
        MainWindow.setCentralWidget(self.shadowPadding)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.titleBarCloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.colorHueSlider.setVisible)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.colorSaturationLabel.setVisible)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.colorSaturationSlider.setVisible)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.colorBrightnessLabel.setVisible)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.colorBrightnessSlider.setVisible)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.camSaturationLabel.setHidden)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.camSaturationSlider.setHidden)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.camBrightnessLabel.setHidden)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.camBrightnessSlider.setHidden)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.camContrastLabel.setHidden)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.camContrastSlider.setHidden)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.camGainLabel.setHidden)
        QtCore.QObject.connect(self.colorHueCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.camGainSlider.setHidden)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.titleLabel.setText(_translate("MainWindow", "Ambient Light Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.samplerTab), _translate("MainWindow", "SAMPLER", None))
        self.fadeDurationLabel.setText(_translate("MainWindow", "FADE DURATION (200ms)", None))
        self.colorHueLabel.setText(_translate("MainWindow", "FIXED COLOR HUE", None))
        self.colorSaturationLabel.setText(_translate("MainWindow", "SATURATION", None))
        self.colorBrightnessLabel.setText(_translate("MainWindow", "BRIGHTNESS", None))
        self.camSaturationLabel.setText(_translate("MainWindow", "CAMERA SATURATION", None))
        self.camBrightnessLabel.setText(_translate("MainWindow", "CAMERA BRIGHTNESS", None))
        self.camContrastLabel.setText(_translate("MainWindow", "CAMERA CONTRAST", None))
        self.camGainLabel.setText(_translate("MainWindow", "CAMERA GAIN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.colorsTab), _translate("MainWindow", "COLORS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serverTab), _translate("MainWindow", "SERVER", None))
        self.statusBarWarningLabel.setText(_translate("MainWindow", "33", None))
        self.statusLabel.setText(_translate("MainWindow", "Connected to server (192.168.1.70:31337)", None))

import ui.main_window_rc
