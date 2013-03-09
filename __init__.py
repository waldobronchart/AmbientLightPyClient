__author__ = 'Waldo'

import sys
from PyQt4 import QtGui, QtCore
import window

## Open up the window
app = QtGui.QApplication(sys.argv)
window.show()
sys.exit(app.exec_())
