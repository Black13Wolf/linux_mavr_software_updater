import urllib.request
import json
proxies = {
    "http" : "http://squid.sao.ru:8080",
    "https" : "http://squid.sao.ru:8080",
}
proxy_support = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
with urllib.request.urlopen('https://api.github.com/repos/Black13Wolf/linux_mavr_software/tags') as url:
    data = json.loads(url.read().decode())
last_update = data[0]
from pip import main as pip
pip(['install', last_update['tarball_url'], '--proxy=http://squid.sao.ru:8080'])