__author__ = 'Waldo'

from PyQt4 import QtGui, QtCore
import ui
from widget_sampler import Sampler
from logger import log
import preferences
Preferences = preferences.Preferences.Instance


# todo: server tab
# todo: write a statusbar logger
# todo: make window shadow transparent to events
# todo: color tab value conversions
class MainWindow(QtGui.QMainWindow):
    Instance = None

    def __init__(self):
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

        # Setup drop shadow effects
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(20)
        dropShadowEffect.setColor(QtGui.QColor("#000000"))
        dropShadowEffect.setOffset(0,0)
        self.ui.shadowPadding.setGraphicsEffect(dropShadowEffect)
        self.addDropShadowToText(self.ui.titleLabel)
        self.addDropShadowToText(self.ui.statusBarWarningLabel)
        self.addDropShadowToText(self.ui.statusLabel)

        # The Sampler widget (this allows for selection of the tv sample bounds)
        self.sampler = Sampler(self.ui.samplerTab)
        self.sampler.nodesUpdated.connect(self.on_sampler_nodesUpdated)

        # The colors tab
        self.initializeColorsTab()

        # All done
        self.initialized = True

    def initializeColorsTab(self):
        self.ui.fadeDurationSlider.setValue(Preferences.fadeDelayMs)

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

    def addDropShadowToText(self, label):
        dropShadowEffect = QtGui.QGraphicsDropShadowEffect(self)
        dropShadowEffect.setBlurRadius(0)
        dropShadowEffect.setColor(QtGui.QColor("#343434"))
        dropShadowEffect.setOffset(0,1)
        label.setGraphicsEffect(dropShadowEffect)

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
        if self.titleBarClicked and e.button() == QtCore.Qt.LeftButton:
            self.titleBarClicked = False

    def closeEvent(self, e):
        log.debug("Window closing")
        self.updateAndSaveSettings()

    def on_tabWidget_currentChanged(self, index):
        if isinstance(index, int):
            # Shamelessly position the arrow over the currently selected tab
            arrowOffset = QtCore.QPoint(198, 22)
            tabRect = self.ui.tabWidget.tabBar().tabRect(index)
            self.ui.tabSelectionArrow.move(tabRect.center() + arrowOffset)

    def on_sampler_nodesUpdated(self):
        self.updateAndSaveSettings()

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
        Preferences.fadeDelayMs = self.ui.fadeDurationSlider.value()
        Preferences.fixedColorEnabled = self.ui.colorHueCheckBox.isChecked()
        Preferences.colorHue = self.ui.colorHueSlider.value()
        Preferences.colorSaturation = self.ui.colorSaturationSlider.value()
        Preferences.colorBrightness = self.ui.colorBrightnessSlider.value()
        Preferences.camSaturation = self.ui.camSaturationSlider.value()
        Preferences.camBrightness = self.ui.camBrightnessSlider.value()
        Preferences.camContrast = self.ui.camContrastSlider.value()
        Preferences.camGain = self.ui.camGainSlider.value()

        preferences.savePreferences()


## Show the main window
def show():
    instance = MainWindow.Instance
    if instance is None:
        instance = MainWindow()
    instance.show()