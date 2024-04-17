import argparse
import time
from loguru import logger
from .clash import Clash


def read_cli_args():
    parser = argparse.ArgumentParser()
    # Options
    parser.add_argument('--url', '-u', default='http://127.0.0.1:9090', help='clash-api 可查看config.yaml文件')
    parser.add_argument('--secret', '-P', default='', help='密码')
    parser.add_argument('--delay', '-T', default=20, type=int, help='自动切换节点间隔时间 单位:秒')
    parser.add_argument('--node-timeout', '-t', default=6, type=int, help='节点超时时间 单位:秒')
    parser.add_argument('--verify-url', default='https://www.google.com', help='用于测试延时的url')
    parser.add_argument('--group-name', default='', help='指定策略组,可通过 --show-group参数查询可用策略组')

    parser.add_argument('--show-group', '-g', action='store_true', default=False, help='查看所有策略组')
    parser.add_argument('--show-proxies', '-p', action='store_true', default=False, help='查看所有代理')
    parser.add_argument('--show-selected', '-s', action='store_true', default=False, help='查看已选择代理')
    return parser.parse_args()


def main():
    args = read_cli_args()
    clash = Clash(
        base_api=args.url,
        secret=args.secret,
        group_name=args.group_name,
        delay_timeout=args.node_timeout,
        verify_url=args.verify_url
    )

    if args.show_group:
        rule_group, selected_rule_group = clash.get_rule_group()
        logger.debug(rule_group)

    if args.show_proxies:
        proxies, selected = clash.get_proxies()
        print(proxies)

    if args.show_selected:
        proxies, selected = clash.get_proxies()
        print(selected)

    if not any([
        args.show_group,
        args.show_proxies,
        args.show_selected
    ]):
        while True:
            clash.auto_switch()
            time.sleep(args.delay)


if __name__ == '__main__':
    main()
