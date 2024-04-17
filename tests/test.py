import time
from easy_clash_tool.clash import Clash

clash = Clash(
    base_api='http://127.0.0.1:24621',
    secret='0367e21c-cceb-43a8-a2db-ad990e80dc28',
    group_name='',
)

# 手动切换
nodes, selected = clash.get_proxies()
print(nodes)
clash.change_node('🎮 Steam 商店/社区')

# 自动切换
while True:
    clash.auto_switch()
    time.sleep(10)
