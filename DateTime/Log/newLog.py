import logging
log_format = '%(asctime)s - %(name)s - %(levelname)s -%(message)'
logFormat = '%(asctime)s - %(created)f - %(filename)s  - %(funcName)s -' \
            '%(levelname)s - %(levelno)d - %(message)s - %(module)s - %(msecs)d - %(name)s - ' \
            '%(pathname)s - %(process)d - %(processName)s - %(relativeCreated)s - %(thread)d - %(threadName)s '

logger = logging.getLogger(__name__)

#To override the default severity of logging
logger.setLevel('DEBUG')

#use FileHandler() to log to a file
#file_handler = logging.FileHandler('mylog.log')
file_handler = logging.StreamHandler()
formatter = logging.Formatter(logFormat) #log_format)
file_handler.setFormatter(formatter)

#Add the handler
logger.addHandler(file_handler)

logger.info("I am a separate Logger")
logger.debug('Try to run this')
logger.warning('I am a message')

