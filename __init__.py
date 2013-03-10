__author__ = 'Waldo'

import sys
from PyQt4 import QtGui, QtCore

# Load prefs from file
from preferences import loadPreferences, savePreferences
loadPreferences()

# Open up the window
import window
app = QtGui.QApplication(sys.argv)
window.show()
app.exec_()

# Save preferences before exit
savePreferences()
sys.exit()
