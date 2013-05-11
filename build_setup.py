import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable("__init__.py", 
	targetName = "AmbiLight.exe", 
	icon = "icon/AmbiLight_Icon.ico",
	base = base)

setup(name = "AmbiLightPyClient",
    version = "1.0",
    description = "It's awesome!",
    options = {"build_exe" : {"includes" : "atexit" }},
    executables = [exe])