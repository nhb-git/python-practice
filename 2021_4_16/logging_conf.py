"""
logging读取conf配置记录日志.
"""
import logging
import logging.config


logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.debug('DEBUG logging message')
