"""
使用yaml配置文件记录日志, logging.
"""
import logging
import logging.config
import yaml


with open('logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
logger.debug('Debug logging message')
