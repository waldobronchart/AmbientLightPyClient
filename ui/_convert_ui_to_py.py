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

# Main Window
subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyrcc4.exe -py3 main_window.qrc > main_window_rc.py", shell=True)
subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyuic4.bat main_window.ui > main_window.py")
replace_in_file('main_window.py', 'import main_window_rc', 'import ui.main_window_rc')

print("done")