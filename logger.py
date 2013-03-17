import logging
import os
import time

log = logging.getLogger('AmbientLightPyClient')
log.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]\t%(message)s')

# Add console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)

# Add file handler
if not os.path.exists('logs'):
    os.makedirs('logs')

fileHandler = logging.FileHandler('logs/ambilight_client.log')
fileHandler.setFormatter(formatter)
log.addHandler(fileHandler)

class StatusBarLogger(logging.Handler):
    def __init__(self, mainWindow):
        logging.Handler.__init__(self)
        self.setLevel(logging.DEBUG)
        log.addHandler(self)

        self.mainWindow = mainWindow
        self.prevLevel = 0
        self.prevLogTime = time.time()
        self.logCount = 0

    def emit(self, record):
        # Set log count
        self.logCount += 1
        self.mainWindow.ui.statusBarCountLabel.setText(str(self.logCount))
        if record.levelno == logging.DEBUG:
            return

        # Don't log if level is lower and has not logged for 5 secs yet
        if record.levelno < self.prevLevel:
            if self.prevLogTime + 5 > time.time():
                return

        # Switch icon if needed
        if record.levelno != self.prevLevel:
            if record.levelno == logging.WARNING:
                self.mainWindow.ui.statusBarIconInfo.hide()
                self.mainWindow.ui.statusBarIconWarning.show()
                self.mainWindow.ui.statusBarIconError.hide()
            elif record.levelno in [logging.ERROR, logging.CRITICAL]:
                self.mainWindow.ui.statusBarIconInfo.hide()
                self.mainWindow.ui.statusBarIconWarning.hide()
                self.mainWindow.ui.statusBarIconError.show()
            else:
                self.mainWindow.ui.statusBarIconInfo.show()
                self.mainWindow.ui.statusBarIconWarning.hide()
                self.mainWindow.ui.statusBarIconError.hide()

        self.prevLogTime = time.time()
        self.prevLevel = record.levelno
        self.mainWindow.ui.statusLabel.setText(self.format(record))