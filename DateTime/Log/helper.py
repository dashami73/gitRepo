import logging

log_format ='%(asctime)s :: %(levelname)s :: %(name)s :: %(filename)s :: %(lineno)d :: %(process)d :: %(message)s'
logging.basicConfig(filename='basic.log', encoding='utf-8', level=logging.DEBUG, filemode='w', format=log_format)

logging.debug('I am a debug log from helper')
