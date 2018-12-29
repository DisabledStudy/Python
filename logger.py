import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='log', format=fmt)
logger = logging.getLogger('loger')

logger.debug('hello ')
logger.critical('world!')