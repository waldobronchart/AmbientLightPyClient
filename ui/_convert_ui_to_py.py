__author__ = 'Waldo'

import os
import subprocess

def replace_in_file(path, source, replacement):
    file = open(path)
    fulltext = file.read()
    file.close()

    file = open(path, 'w')
    fulltext = fulltext.replace(source, replacement)
    file.write(fulltext)
    file.close()

# Resources
subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyrcc4.exe -py3 titlebar.qrc > titlebar_rc.py", shell=True)
subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyrcc4.exe -py3 statusbar.qrc > statusbar_rc.py", shell=True)

# UI's
subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyuic4.bat main_window.ui > main_window.py")
subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyuic4.bat titlebar.ui > titlebar.py")
subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyuic4.bat statusbar.ui > statusbar.py")

# Python fixup for each UI
replace_in_file('main_window.py', 'import main_window_rc', 'import ui.main_window_rc')
replace_in_file('titlebar.py', 'import titlebar_rc', 'import ui.titlebar_rc')
replace_in_file('statusbar.py', 'import statusbar_rc', 'import ui.statusbar_rc')

print("done")