import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin
from typing import Tuple, List
import requests
from easy_spider_tool import jsonpath, retry
from loguru import logger
from requests import RequestException


class Clash:
    def __init__(self, base_api: str = 'http://127.0.0.1:9090', group_name: str = '', delay_timeout: int = 6,
                 verify_url: str = 'https://www.google.com',
                 secret=''):
        self.base_api = base_api
        self.group_name = group_name
        self.delay_timeout = delay_timeout
        self.verify_url = verify_url
        self.secret = secret

        self.headers = {'Authorization': f'Bearer {secret}'} if secret else {}

    def get_rule_group(self) -> Tuple[List[str], str]:
        """获取策略组名称"""
        api_url = urljoin(self.base_api, f'proxies')
        response = requests.get(api_url, timeout=10, headers=self.headers, verify=False)
        rule_group = jsonpath(response.json(), f'$.proxies[?(@.type=="Selector")].name', first=False, default=[])
        selected_rule_group = rule_group[0]
        return rule_group, selected_rule_group

    @retry(num=1, )
    def get_proxies(self) -> Tuple[List[str], str]:
        """获取策略组中的所有节点"""
        api_url = urljoin(self.base_api, f'proxies')
        response = requests.get(api_url, timeout=10, headers=self.headers, verify=False)
        all_proxies = jsonpath(response.json(), f'$.proxies.{self.group_name}.all[*]', first=False, default=[])
        selected = jsonpath(response.json(), f'$.proxies.{self.group_name}.now', first=True, default='')
        return all_proxies, selected

    def verify_proxy(self, name: str, verify_url: str = None, timeout: int = None, retry_num: int = 1):
        """验证节点"""
        if not timeout:
            timeout = self.delay_timeout
        if not verify_url:
            verify_url = self.verify_url
        api = urljoin(self.base_api, f'/proxies/{name}/delay?timeout={timeout * 1000}&url={verify_url}')
        retry_count = 0
        while retry_num >= retry_count:
            try:
                response = requests.get(api, headers=self.headers, timeout=timeout, verify=False)
                if response is not None:
                    err_info = response.json().get('message', '')
                    if err_info:
                        logger.error(f'<{name}> {err_info}')
                        break
                    delay = response.json().get('delay', 0)
                    return name, delay
            except RequestException as rex:
                # logger.error(f'request exception: {rex}')
                retry_count += 1
        return None, None

    @retry(num=1)
    def change_node(self, name: str):
        """更换节点"""
        api = f'{self.base_api}/proxies/{self.group_name}'
        headers = {
            'Content-Type': 'application/json',
            **self.headers
        }
        payload = json.dumps({
            "name": f"{name}"
        })
        response = requests.put(api, headers=headers, data=payload, timeout=10, verify=False)
        if response is not None:
            if response.status_code == 204:
                return True
            err_info = response.json().get('message', '')
            if err_info:
                logger.error(f'{err_info}')
        return False

    def auto_switch(self):
        """自动切换可用节点"""
        if not self.group_name:
            rule_group, self.group_name = self.get_rule_group()
            logger.debug(f'可选策略组:{rule_group}')
            logger.warning(f'默认选中策略组:<{self.group_name}>')

        proxies, selected = self.get_proxies()

        available_nodes = []
        if selected:
            proxy_name, delay = self.verify_proxy(name=selected)
            if delay is not None:
                logger.success(f'[{self.group_name}] <{selected}> 延迟:{delay}ms -> 节点正常')
                return None

            proxies.remove(selected)

        with ThreadPoolExecutor(max_workers=20) as pool:
            futures = [pool.submit(self.verify_proxy, proxy_name) for proxy_name in proxies]
            for future in as_completed(futures):
                try:
                    proxy_name, delay = future.result()
                    if delay is not None and delay > 0:
                        available_nodes.append((proxy_name, delay))
                        break
                except Exception as ex:
                    logger.exception(f'{ex}')

        # 更换可用节点
        if len(available_nodes):
            logger.debug(f'可用节点数: {len(available_nodes)}')
            min_delay_node = min(available_nodes, key=lambda x: x[1])
            if min_delay_node:
                if self.change_node(min_delay_node[0]):
                    logger.success(
                        f'[{self.group_name}] <{min_delay_node[0]}> 延迟:{min_delay_node[1]}ms -> 切换到节点')
                else:
                    logger.error(
                        f'[{self.group_name}] <{min_delay_node[0]}> 延迟:{min_delay_node[1]}ms -> 切换到节点失败')
        else:
            logger.error(f'[{self.group_name}] -> 未找到可用节点')
