"""
logging.
"""
import logging
import logging.handlers
import datetime


# 使用logging本身的日志等级
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This is a debug log.')
# logging.log(logging.DEBUG, "This is a debug log.")
# logging.log(logging.WARNING, "This is a warning log.")


# 使用logging的四大组件
# 创建日志器
logger = logging.getLogger('mylogger')
# 设置日志等级
logger.setLevel(logging.DEBUG)
# 创建handler
rf_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0)
)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
