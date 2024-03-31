# easy-clash-tool

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/easy-clash-tool)
![PyPI - Version](https://img.shields.io/pypi/v/easy-clash-tool)
![PyPI - License](https://img.shields.io/pypi/l/easy-clash-tool)
![PyPI - Format](https://img.shields.io/pypi/format/easy-clash-tool)
![GitHub watchers](https://img.shields.io/github/watchers/hanxinkong/easy-clash-tool)
![GitHub forks](https://img.shields.io/github/forks/hanxinkong/easy-clash-tool)
![GitHub Repo stars](https://img.shields.io/github/stars/hanxinkong/easy-clash-tool)

## 简介

easy_clash_tool是一个clash的python库,可以很便捷的自动切换可用节点，希望能为使用者带来益处。如果您也想贡献好的代码片段，请将代码以及描述，通过邮箱（ [xinkonghan@gmail.com](mailto:hanxinkong<xinkonghan@gmail.com>)
）发送给我。代码格式是遵循自我主观，如存在不足敬请指出！

----
**文档地址：
** <a href="https://easy-clash-tool.xink.top/" target="_blank">https://easy-clash-tool.xink.top/ </a>

**PyPi地址：
** <a href="https://pypi.org/project/easy-clash-tool" target="_blank">https://pypi.org/project/easy-clash-tool </a>

**GitHub地址：
** [https://github.com/hanxinkong/easy-clash-tool](https://github.com/hanxinkong/easy-clash-tool)

----

## 安装

<div class="termy">

```console
pip install easy-clash-tool
```

</div>

## 简单使用

### demo.py

```python
from easy_clash_tool.clash import Clash

clash = Clash(
    base_api='http://127.0.0.1:9090',
)
clash.clash_cli(timeout=10)
```

![img.png](res%2Fimg.png)

参数说明

| 字段名           | 类型     | 必须 | 描述                                       |
|---------------|--------|----|------------------------------------------|
| base_api      | string | 否  | clash_api地址端口（默认: http://127.0.0.1:9090） |
| group_name    | string | 否  | 策略组（默认: GLOBAL）                          |
| delay_timeout | string | 否  | 节点超时时间（默认: 6秒）                           |
| verify_url    | string | 否  | 测试超时的站点（默认: https://www.google.com）      |
| secret        | string | 否  | 安全密钥                                     |

命令行

```shell
usage: demo.py [-h] [--show-group] [--show-proxies] [--show-selected]

optional arguments:
  -h, --help           show this help message and exit
  --show-group, -g     查看所有策略组
  --show-proxies, -p   查看所有代理
  --show-selected, -s  查看已选择代理
```

## 链接

Github：https://github.com/hanxinkong/easy-clash-tool

在线文档：https://easy-clash-tool.xink.top

## 贡献者

## 许可证

该项目根据 **MIT** 许可条款获得许可.

## 免责声明

1. 若使用者滥用本项目,本人 **无需承担** 任何法律责任.
2. 本程序仅供娱乐,源码全部开源,**禁止滥用** 和二次 **贩卖盈利**.  **禁止用于商业用途**.
