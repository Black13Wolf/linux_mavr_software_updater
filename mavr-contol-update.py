import urllib.request
import json
proxies = {
    "http" : "http://squid.sao.ru:8080",
    "https" : "http://squid.sao.ru:8080",
}
print(proxies)
proxy_support = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
with urllib.request.urlopen('https://api.github.com/repos/Black13Wolf/linux_mavr_software/tags') as url:
    data = json.loads(url.read().decode())
print(data)
print(type(data))