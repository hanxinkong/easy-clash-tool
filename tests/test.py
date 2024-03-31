from easy_clash_tool.clash import Clash

clash = Clash(
    base_api='http://127.0.0.1:56302',
    secret='0367e21c-cceb-43a8-a2db-ad990e80dc28'
)
clash.clash_cli(timeout=10)
