import socket
import threading
import time

from server_messages import NetMessage, NetMessageType
from logger import log

class IncomingMessage(object):
    def __init__(self, id, type, data, size, addrFrom):
        self.id = id
        self.type = type
        self.data = data
        self.size = size
        self.addrFrom = addrFrom

class ServerCommunication(object):
    Instance = None

    def __init__(self):
        ServerCommunication.Instance = self
        self.socket = None
        self.isConnected = False
        self.incomingMessages = []
        self._tryToConnect = False
        self._quit = False

        self.thread = threading.Thread(target=self._threadFuncReadIncoming)
        self.thread.start()

    def connectTo(self, ip, port):
        if self.isConnected:
            self.disconnect()

        self.addr = (ip, port)
        log.info("Connecting to server... (%s:%s)" % (ip, port))
        if self.socket is None:
            self.socket = socket.socket()
        self._tryToConnect = True

    def _threadFuncReadIncoming(self):
        while True:
            try:
                if self._quit:
                    break

                if not self.isConnected and self._tryToConnect:
                    try:
                        self.socket.connect(self.addr)
                        self.isConnected = True
                        log.info("Connected to server!")
                    except Exception as ex:
                        log.warn("Failed to connect to server: %s", ex.__class__.__name__)
                        log.debug("... reason for failure: %s", ex)
                        self.isConnected = False
                    self._tryToConnect = False

                if not self.isConnected:
                    time.sleep(0.5)

                if self.isConnected:
                    # Get header
                    data, addr = self.socket.recvfrom(NetMessage.HEADER_LENGTH)
                    msgid = int(data[:4])
                    msgsize = int(data[5:])
                    type = NetMessageType.CLASS_LOOKUP[msgid]

                    # Get body based on header
                    totalSizeReceived = 0
                    data = b''
                    while totalSizeReceived < msgsize:
                        data_part, addr = self.socket.recvfrom(msgsize - totalSizeReceived)
                        data += data_part
                        totalSizeReceived = len(data)

                    # Completed receiving full message
                    log.debug("Received message '%s' (%sbytes)", type.__name__, msgsize)
                    inMsg = IncomingMessage(msgid, type, data, msgsize, addr)
                    self.incomingMessages.append(inMsg)

            except (ConnectionResetError, ConnectionAbortedError):
                log.debug("Connection lost")
                self.isConnected = False
                self.socket = None

            except Exception as ex:
                log.error("Exception in thread: %s", ex.__class__.__name__)
                log.debug("... exception details: %s", ex)
                break

        self.isConnected = False
        log.debug("THREAD ENDED!")

    def disconnect(self):
        self._tryToConnect = False
        if self.isConnected:
            log.debug("Disconnecting")
            self.isConnected = False
            self.socket.close()

    def stopThread(self):
        self._quit = True

    def processIncomingMessages(self):
        if not len(self.incomingMessages):
            return

        for msg in self.incomingMessages:
            log.debug("Reading message '%s' (%sbytes)", msg.type.__name__, msg.size)
            msgClass = NetMessageType.CLASS_LOOKUP[msg.id]
            msgInstance = msgClass()
            msgInstance.read(msg.data.decode("utf-8"))

        # Empty the list
        self.incomingMessages = []

    def sendMessage(self, msg):
        if not self.isConnected:
            return

        msgSerialized = msg.serialize()
        log.debug("Sending message '%s' (%sbytes)", msg.__class__.__name__, len(msgSerialized))
        self.socket.send(msgSerialized.encode('utf-8'))
