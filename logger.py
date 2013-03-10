import logging
import os

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