__author__ = 'Waldo'

import os
import subprocess

subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyrcc4.exe -py3 resources.qrc > resources_rc.py", shell=True)

subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyuic4.bat main_window.ui > main_window.py")
subprocess.call("C:\Python33\Lib\site-packages\PyQt4\pyuic4.bat titlebar.ui > titlebar.py")

def replace_in_file(path, source, replacement):
    file = open(path)
    fulltext = file.read()
    file.close()

    file = open(path, 'w')
    fulltext = fulltext.replace(source, replacement)
    file.write(fulltext)
    file.close()

replace_in_file('main_window.py', 'import resources_rc', 'import ui.resources_rc')
replace_in_file('titlebar.py', 'import resources_rc', 'import ui.resources_rc')

print("done")