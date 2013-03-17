import os
import json
from logger import log
from config import *

class Preferences(object):
    Instance = None

    def __init__(self):
        self.windowPos = [0, 0]
        self.serverIp = '192.168.1.200'
        self.serverPort = 13555

        self.boundsTopLeft = [0.2, 0.2]
        self.boundsTopRight = [0.8, 0.2]
        self.boundsBottomRight = [0.8, 0.8]
        self.boundsBottomLeft = [0.2, 0.8]

        self.totalFadeTimeMS = 200

        self.fixedColorEnabled = False
        self.colorHue = 20
        self.colorSaturation = 255
        self.colorBrightness = 0

        self.camSaturation = 117
        self.camBrightness = 30
        self.camContrast = 74
        self.camGain = 204

## Load prefs from file
def loadPreferences():
    log.info("Loading preferences from file: %s", PREFERENCES_FILE)
    Preferences.Instance = Preferences()

    if not os.path.exists(PREFERENCES_FILE):
        log.info("...preferences file does not exist. Using defaults!")
        return

    try:
        file = open(PREFERENCES_FILE)

        # Merge the two together
        new_prefs = json.loads(file.read())

        for attr, value in new_prefs.items():
            if attr in Preferences.Instance.__dict__.keys():
                Preferences.Instance.__setattr__(attr, value)
                log.debug(" - %s = %s", attr, value)
        
        file.close()
        log.info("Preferences loaded")

    except Exception as ex:
        log.error("Failed to load preferences from file", ex)

## Save prefs
def savePreferences():
    log.info("Saving preferences to file: %s", PREFERENCES_FILE)
    jsonStr = json.dumps(Preferences.Instance.__dict__, sort_keys=True, indent=4)
    file = open(PREFERENCES_FILE, 'w')
    file.write(jsonStr)
    file.close()
    log.info("Preferences saved")