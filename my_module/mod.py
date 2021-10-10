import yaml
from logging import getLogger, config

with open('./my_module/logger_conf.yaml', encoding='utf-8') as file:
    config.dictConfig(yaml.safe_load(file))
logger = getLogger(__name__)


def hoge():
    logger.debug('debug msg')
    logger.info('info msg')
    logger.warning('warning msg')
    logger.error('error msg')
    logger.critical('critical msg')


if __name__ == '__main__':
    hoge()
