import yaml
from logging import getLogger, config
from my_module import mod

with open('./my_module/logger_conf.yaml', encoding='utf-8') as file:
    config.dictConfig(yaml.safe_load(file))
logger = getLogger(__name__)

# --- ログ出力 ---
logger.debug('debug msg')
logger.info('info msg')
logger.warning('warning msg')
logger.error('error msg')
logger.critical('critical msg')

mod.hoge()
