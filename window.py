import colorsys

__author__ = 'Waldo'

from PyQt4 import QtGui, QtCore
import ui
from widget_sampler import Sampler
from logger import log, StatusBarLogger
from server_communication import ServerCommunication
import preferences
Preferences = preferences.Preferences.Instance

# todo: test servercommunication
# todo: sampler tab loading frame?
# todo: server tab not connected warning
# todo: make it an exe or bat?
class MainWindow(QtGui.QMainWindow):
    Instance = None

    def __init__(self):
        log.debug("initializing MainWindow")
        super(MainWindow, self).__init__()
        MainWindow.Instance = self
        self.titleBarClicked = False
        self.initialized = False

        # Setup
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.ui = ui.Ui_MainWindow()
        self.window_handle = self.ui.setupUi(self)
        self.move(Preferences.windowPos[0], Preferences.windowPos[1])
        self.ui.tabWidget.setCurrentIndex(1)

        # Status bar
        self._addDropShadowToText(self.ui.statusBarCountLabel, "#343434")
        self._addDropShadowToText(self.ui.statusLabel, "#343434")
        self.statusBarLogger = StatusBarLogger(self)

        # Setup drop shadow effect on window
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(20)
        dropShadowEffect.setColor(QtGui.QColor("#000000"))
        dropShadowEffect.setOffset(0,0)
        self.ui.shadowPadding.setGraphicsEffect(dropShadowEffect)
        self._addDropShadowToText(self.ui.titleLabel, "#343434")

        # The Sampler widget (this allows for selection of the tv sample bounds)
        self.sampler = Sampler(self.ui.samplerTab)
        self.sampler.nodesUpdated.connect(self.on_sampler_nodesUpdated)

        # Color tab
        self.updateColorTabFromSettings()
        self._addDropShadowToText(self.ui.fadeDurationLabel, "#121618")
        self._addDropShadowToText(self.ui.colorHueLabel, "#121618")
        self._addDropShadowToText(self.ui.colorSaturationLabel, "#121618")
        self._addDropShadowToText(self.ui.colorBrightnessLabel, "#121618")
        self._addDropShadowToText(self.ui.camSaturationLabel, "#121618")
        self._addDropShadowToText(self.ui.camBrightnessLabel, "#121618")
        self._addDropShadowToText(self.ui.camContrastLabel, "#121618")
        self._addDropShadowToText(self.ui.camGainLabel, "#121618")

        # Server tab
        ipValidator = QtGui.QRegExpValidator()
        ipValidator.setRegExp(QtCore.QRegExp("((1{0,1}[0-9]{0,2}|2[0-4]{1,1}[0-9]{1,1}|25[0-5]{1,1})\\.){3,3}(1{0,1}[0-9]{0,2}|2[0-4]{1,1}[0-9]{1,1}|25[0-5]{1,1})"))
        self.ui.ipField.setValidator(ipValidator)
        self.ui.ipField.setText(Preferences.serverIp)
        self._addDropShadowToText(self.ui.ipLabel, "#121618")

        portValidator = QtGui.QRegExpValidator()
        portValidator.setRegExp(QtCore.QRegExp("([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])"))
        self.ui.portField.setValidator(portValidator)
        self.ui.portField.setText(str(Preferences.serverPort))
        self._addDropShadowToText(self.ui.portLabel, "#121618")

        # Server communication
        self.serverComm = ServerCommunication()
        self.serverComm.connectTo(Preferences.serverIp, Preferences.serverPort)
        self.updateLoopTimer = QtCore.QTimer()
        self.updateLoopTimer.setSingleShot(False)
        self.updateLoopTimer.timeout.connect(self.updateLoop)
        self.updateLoopTimer.start(33.33)
        self.frameGrabTimer = QtCore.QTimer()
        self.frameGrabTimer.setSingleShot(False)
        self.frameGrabTimer.timeout.connect(self.requestFrame)
        self.frameGrabTimer.start(2000)
        
        # All done
        self.initialized = True

    def updateColorTabFromSettings(self):
        self.ui.fadeDurationSlider.setValue(Preferences.totalFadeTimeMS)

        self.ui.colorHueCheckBox.setChecked(Preferences.fixedColorEnabled)
        self.ui.colorHueSlider.setValue(Preferences.colorHue)
        self.ui.colorSaturationSlider.setValue(Preferences.colorSaturation)
        self.ui.colorBrightnessSlider.setValue(Preferences.colorBrightness)

        self.ui.camSaturationSlider.setValue(Preferences.camSaturation)
        self.ui.camBrightnessSlider.setValue(Preferences.camBrightness)
        self.ui.camContrastSlider.setValue(Preferences.camContrast)
        self.ui.camGainSlider.setValue(Preferences.camGain)

        # Color tab check and uncheck to refresh ui
        self.ui.colorHueCheckBox.toggle()
        self.ui.colorHueCheckBox.toggle()

    def _addDropShadowToText(self, label, hexCode):
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(0)
        dropShadowEffect.setColor(QtGui.QColor(hexCode))
        dropShadowEffect.setOffset(0,1)
        label.setGraphicsEffect(dropShadowEffect)

    def updateLoop(self):
        # Slow update loop if not connected
        if not self.serverComm.isConnected:
            self.updateLoopTimer.setInterval(5000)
            self.ui.connectButton.show()
            
        self.serverComm.processIncomingMessages()

    def requestFrame(self):
        if self.serverComm.isConnected and self.ui.tabWidget.currentIndex() == 0:
            log.info("Requesting frame from server...")
            from server_messages import MsgGenericRequest
            msg = MsgGenericRequest("getframebuffer")
            self.serverComm.sendMessage(msg)

    def mousePressEvent(self, e):
        # Is mouse over the titlebar?
        titleBarPosInWindow = self.ui.titleBar.mapTo(self, self.ui.titleBar.pos())
        if self.ui.titleBar.rect().contains(e.pos() - titleBarPosInWindow):
            self.titleBarClicked = (e.button() == QtCore.Qt.LeftButton)
            if self.titleBarClicked:
                self.titleBarMoveMouseStart = e.globalPos() - self.pos()

    def mouseMoveEvent(self, e):
        if self.titleBarClicked:
            self.move(e.globalPos() - self.titleBarMoveMouseStart)

    def mouseReleaseEvent(self, e):
        self.setFocus(QtCore.Qt.MouseFocusReason)
        if self.titleBarClicked and e.button() == QtCore.Qt.LeftButton:
            self.titleBarClicked = False

    def closeEvent(self, e):
        log.debug("Window closing")
        self.serverComm.disconnect()
        self.serverComm.stopThread()
        self.updateAndSaveSettings()

    def on_tabWidget_currentChanged(self, index):
        if isinstance(index, int):
            # Shamelessly position the arrow over the currently selected tab
            arrowOffset = QtCore.QPoint(198, 22)
            tabRect = self.ui.tabWidget.tabBar().tabRect(index)
            self.ui.tabSelectionArrow.move(tabRect.center() + arrowOffset)

    def on_sampler_nodesUpdated(self):
        self.updateAndSaveSettings()
        from server_messages import MsgSetBounds
        self.serverComm.sendMessage(MsgSetBounds())

    def on_fadeDurationSlider_valueChanged(self, value):
        self.ui.fadeDurationLabel.setText("FADE DURATION (%ims)" % value)

    def on_fadeDurationSlider_sliderReleased(self):
        log.debug("fadeDuration set to %ims" % self.ui.fadeDurationSlider.value())
        self.updateAndSaveSettings()

    def on_colorHueCheckBox_toggled(self, checked):
        log.debug("fixedColorEnabled set to %s" % checked)
        self.updateAndSaveSettings()

    def on_colorHueSlider_sliderReleased(self):
        log.debug("colorHue set to %i" % self.ui.colorHueSlider.value())
        self.updateAndSaveSettings()

    def on_colorSaturationSlider_sliderReleased(self):
        log.debug("colorSaturation set to %i" % self.ui.colorSaturationSlider.value())
        self.updateAndSaveSettings()

    def on_colorBrightnessSlider_sliderReleased(self):
        log.debug("colorBrightness set to %i" % self.ui.colorBrightnessSlider.value())
        self.updateAndSaveSettings()

    def on_camSaturationSlider_sliderReleased(self):
        log.debug("camSaturation set to %i" % self.ui.camSaturationSlider.value())
        self.updateAndSaveSettings()

    def on_camBrightnessSlider_sliderReleased(self):
        log.debug("camBrightness set to %i" % self.ui.camBrightnessSlider.value())
        self.updateAndSaveSettings()

    def on_camContrastSlider_sliderReleased(self):
        log.debug("camContrast set to %i" % self.ui.camContrastSlider.value())
        self.updateAndSaveSettings()

    def on_camGainSlider_sliderReleased(self):
        log.debug("camGain set to %i" % self.ui.camGainSlider.value())
        self.updateAndSaveSettings()

    def on_ipField_editingFinished(self):
        if Preferences.serverIp != self.ui.ipField.text():
            self.serverEndpointChanged()

    def on_portField_editingFinished(self):
        if Preferences.serverPort != int(self.ui.portField.text()):
            self.serverEndpointChanged()

    def serverEndpointChanged(self):
        log.debug("serverEndpoint set to %s:%s" % (self.ui.ipField.text(), self.ui.portField.text()))
        Preferences.serverIp = self.ui.ipField.text()
        Preferences.serverPort = int(self.ui.portField.text())
        preferences.savePreferences()
        self.ui.connectButton.show()

    def on_connectButton_clicked(self, *args):
        if not args:
            self.serverComm.connectTo(Preferences.serverIp, Preferences.serverPort)
            self.ui.connectButton.hide()

    def updateAndSaveSettings(self):
        if not self.initialized:
            return

        Preferences.windowPos = [self.x(), self.y()]
        
        # Bounds
        width = self.sampler.width()
        height = self.sampler.height()
        topLeft = self.sampler.nodesContainer.topLeft.pos()
        Preferences.boundsTopLeft = [topLeft.x() / width, topLeft.y() / height]
        topRight = self.sampler.nodesContainer.topRight.pos()
        Preferences.boundsTopRight = [topRight.x() / width, topRight.y() / height]
        bottomRight = self.sampler.nodesContainer.bottomRight.pos()
        Preferences.boundsBottomRight = [bottomRight.x() / width, bottomRight.y() / height]
        bottomLeft = self.sampler.nodesContainer.bottomLeft.pos()
        Preferences.boundsBottomLeft = [bottomLeft.x() / width, bottomLeft.y() / height]

        # Color tab
        Preferences.totalFadeTimeMS = self.ui.fadeDurationSlider.value()
        Preferences.fixedColorEnabled = self.ui.colorHueCheckBox.isChecked()
        Preferences.colorHue = self.ui.colorHueSlider.value()
        Preferences.colorSaturation = self.ui.colorSaturationSlider.value()
        Preferences.colorBrightness = self.ui.colorBrightnessSlider.value()
        Preferences.camSaturation = self.ui.camSaturationSlider.value()
        Preferences.camBrightness = self.ui.camBrightnessSlider.value()
        Preferences.camContrast = self.ui.camContrastSlider.value()
        Preferences.camGain = self.ui.camGainSlider.value()

        # debug
        rgb = colorsys.hsv_to_rgb(Preferences.colorHue/100.0, Preferences.colorSaturation/100.0, Preferences.colorBrightness/100.0)
        self.ui.COLORFRAME.setStyleSheet("#COLORFRAME { background: rgb("+str(int(rgb[0]*255))+", "+str(int(rgb[1]*255))+", "+str(int(rgb[2]*255))+"); }")

        # Save and update server
        preferences.savePreferences()
        from server_messages import MsgSetColorSettings
        self.serverComm.sendMessage(MsgSetColorSettings())


## Show the main window
def show():
    instance = MainWindow.Instance
    if instance is None:
        instance = MainWindow()
    instance.show()