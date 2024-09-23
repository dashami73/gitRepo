import logging
#import helper


#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('Brook.log')
#level
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formate = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formate)
file_h.setFormatter(formate)

logger.addHandler(stream_h)
logger.addHandler(file_h)



def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multi(a, b):
    return a * b
def divide(a, b):
    return a / b
def mod(a, b):
    return a % b

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logger.warning('Addition : {} + {} = {}'.format(num_1, num_2, add_result))
sub_result = subtract(num_1, num_2)
logger.error('Subtraction : {} + {} ={}'.format(num_1, num_2, sub_result))
multi_result = multi(num_1, num_2)
logger.debug('Multiplication : {} + {} = {}'.format(num_1, num_2, multi_result))
divid_result = divide(num_1, num_2)
logger.debug('Divide : {} + {} = {}'.format(num_1, num_2, divid_result))
mod_result = mod(num_1, num_2)
logger.debug('Mod : {} + {} = {} '.format(num_1, num_2, mod_result))


'''
log_format ='%(asctime)s :: %(levelname)s :: %(name)s :: %(filename)s :: %(lineno)d :: %(process)d :: %(message)s'
logging.basicConfig(filename='basic.log', encoding='utf-8', level=logging.DEBUG, filemode='w', format=log_format)

logging.debug('This is a debug message')
logging.warning('Warning - careful! something does not look right')
logging.info('This is an information message')
logging.error("An error encounter ")
logging.critical('A message of CRITICAL')
'''