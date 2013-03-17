import json
import colorsys
from logger import log
import preferences
Preferences = preferences.Preferences.Instance

class NetMessageType:
    MSG_INVALID = 0
    MSG_GENERIC_REQUEST = 1
    MSG_GENERIC_REPONSE = 2
    MSG_FRAME_BUFFER = 3
    MSG_PREFERENCES = 4
    MSG_SET_BOUNDS = 5
    MSG_SET_COLOR_SETTINGS = 6
    CLASS_LOOKUP = {}

class NetMessage(object):
    HEADER_LENGTH = 15

    def serialize(self):
        body = json.dumps(self.__dict__)
        data = '%4i,%10i%s\0' % (self.__class__.TYPE, len(body)+1, body)
        return data

    def autoDeserialize(self, strData):
        log.debug("NetMessage.autoDeserialize: ")
        my_attributes = self.__dict__.keys()
        json_data = json.loads(strData)
        for attr in json_data:
            if attr in my_attributes:
                value = json_data[attr]
                log.debug(" - %s = %s", attr, value)
                self.__setattr__(attr, value)

    def write(self):
        return None

    def read(self, strData):
        pass

class MsgGenericRequest(NetMessage):
    TYPE = NetMessageType.MSG_GENERIC_REQUEST
    class REQUEST_STR:
        getframebuffer = "getframebuffer"
        getprefs = "getprefs"

    def __init__(self, requestStr):
        self.request = requestStr

    def write(self):
        return self.serialize()

class MsgGenericResponse(NetMessage):
    TYPE = NetMessageType.MSG_GENERIC_REPONSE
    def __init__(self):
        self.error = None
        self.info = None
        self.warning = None

    def read(self, strData):
        self.autoDeserialize(strData)
        if self.error is not None:
            log.error(self.error)
        if self.info is not None:
            log.info(self.info)
        if self.warning is not None:
            log.warn(self.warning)

class MsgFrameBuffer(NetMessage):
    TYPE = NetMessageType.MSG_FRAME_BUFFER
    def __init__(self):
        self.width = 0
        self.height = 0
        self.imageSize = 0
        self.channelSeq = ""
        self.imageData = []
        self.colorModel = ""

    def read(self, strData):
        self.autoDeserialize(strData)
        if not self.imageData:
            return

        imageData = ""
        for pixel in self.imageData:
            r = (int(pixel) >> 16) & 0b11111111
            g = (int(pixel) >> 8) & 0b11111111
            b = int(pixel) & 0b11111111

            imageData += chr(r) + chr(g) + chr(b)

        # Update sampler
        from window import MainWindow
        MainWindow.Instance.sampler.setFrame(imageData, self.width, self.height)

class MsgPreferences(NetMessage):
    TYPE = NetMessageType.MSG_PREFERENCES

    def read(self, strData):
        json_data = json.loads(strData)

        Preferences.boundsTopLeft = json_data['boundsTopLeft']
        Preferences.boundsTopRight = json_data['boundsTopRight']
        Preferences.boundsBottomRight = json_data['boundsBottomRight']
        Preferences.boundsBottomLeft = json_data['boundsBottomLeft']

        Preferences.totalFadeTimeMS = json_data['totalFadeTimeMS']

        Preferences.fixedColorEnabled = json_data['fixedColorEnabled']
        rgb = json_data['fixedColor']
        hsv = colorsys.rgb_to_hsv(rgb[0]/255.0, rgb[0]/255.0, rgb[0]/255.0)
        Preferences.colorHue = hsv[0]
        Preferences.colorSaturation = hsv[1]
        Preferences.colorBrightness = hsv[2]

        Preferences.camSaturation = json_data['camSaturation']
        Preferences.camBrightness = json_data['camBrightness']
        Preferences.camContrast = json_data['camContrast']
        Preferences.camGain = json_data['camGain']
        
        preferences.savePreferences()

        # Update interface
        from window import MainWindow
        MainWindow.Instance.updateColorTabFromSettings()
        MainWindow.Instance.sampler.setBounds(Preferences.boundsTopLeft, Preferences.boundsTopRight,
                                                Preferences.boundsBottomRight, Preferences.boundsBottomLeft)

        log.info("Updated to server's preferences")


class MsgSetBounds(NetMessage):
    TYPE = NetMessageType.MSG_SET_BOUNDS

    def __init__(self):
        self.boundsTopLeft = Preferences.boundsTopLeft
        self.boundsTopRight = Preferences.boundsTopRight
        self.boundsBottomRight = Preferences.boundsBottomRight
        self.boundsBottomLeft = Preferences.boundsBottomLeft

    def write(self):
        return self.serialize()


class MsgSetColorSettings(NetMessage):
    TYPE = NetMessageType.MSG_SET_COLOR_SETTINGS

    def __init__(self):
        self.totalFadeTimeMS = Preferences.totalFadeTimeMS
        
        self.fixedColorEnabled = Preferences.fixedColorEnabled
        rgbColor = colorsys.hsv_to_rgb(Preferences.colorHue, Preferences.colorSaturation, Preferences.colorBrightness)
        self.fixedColor = (int(rgbColor[0]*255), int(rgbColor[1]*255), int(rgbColor[1]*255))

        self.camSaturation = Preferences.camSaturation
        self.camBrightness = Preferences.camBrightness
        self.camContrast = Preferences.camContrast
        self.camGain = Preferences.camGain

    def write(self):
        return self.serialize()



NetMessageType.CLASS_LOOKUP = {
    NetMessageType.MSG_INVALID              : None,
    NetMessageType.MSG_GENERIC_REQUEST      : MsgGenericRequest,
    NetMessageType.MSG_GENERIC_REPONSE      : MsgGenericResponse,
    NetMessageType.MSG_FRAME_BUFFER         : MsgFrameBuffer,
    NetMessageType.MSG_PREFERENCES          : MsgPreferences,
    NetMessageType.MSG_SET_BOUNDS           : MsgSetBounds,
    NetMessageType.MSG_SET_COLOR_SETTINGS   : MsgSetColorSettings
}