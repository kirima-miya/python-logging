# 概要

`main.py`を実行すると、以下のログが出力される。

```
ex. 時間 ロギングレベル(ロガー名): メッセージ
18:45:35 DEBUG(__main__): debug msg
18:45:35 INFO(__main__): info msg
18:45:35 WARNING(__main__): warning msg
18:45:35 ERROR(__main__): error msg
18:45:35 CRITICAL(__main__): critical msg
18:45:35 DEBUG(my_module.mod): debug msg
18:45:35 INFO(my_module.mod): info msg
18:45:35 WARNING(my_module.mod): warning msg
18:45:35 ERROR(my_module.mod): error msg
18:45:35 CRITICAL(my_module.mod): critical msg
```

# 表示するロギングレベルを変更する

`logger_conf.yaml`の「各ファイルのロガー」の level を変更する。

```yaml
# 各ファイルのロガー
root: # <- main.pyのロガー設定
  level: DEBUG # <- ここ
  handlers: [console]
loggers:
  my_module.mod: # my_module/mod.pyのロガー設定
    level: DEBUG # <- ここ
    handlers: [console]
    propagate: no
```

# ロガーを追加する

以下のコードを追加することでファイル名に応じたロガーを追加できる。

① 任意の Python コード(ex. `my_module/hoge.py`)に追加

```python
import yaml
from logging import getLogger, config

with open('./my_module/logger_conf.yaml', encoding='utf-8') as file:
    config.dictConfig(yaml.safe_load(file))
logger = getLogger(__name__)
```

② `logger_conf.yaml`の`loggers:`に追加

```yaml
# my_module/hoge.pyの場合
loggers:
  my_module.hoge:
    level: DEBUG
    handlers: [console]
    propagate: no
```
