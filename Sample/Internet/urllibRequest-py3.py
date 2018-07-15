# -*- coding: utf-8 -*-
import urllib.request
import urllib.error

try:
    # # 使用代理
    # proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:80'})
    # opener = urllib.request.build_opener(proxy)
    # response = opener.open('https://www.zhihu.com')
    # print(response.read())

    # 最简单例子
    req = urllib.request.Request('https://www.zhihu.com')
    response = urllib.request.urlopen(req)
    html = response.read()
    print(html)
except urllib.error.HTTPError as e: # 服务器错误
    if hasattr(e, 'code'):
        print('Error code:', e.code)
except urllib.error.URLError as e: # 路径不可达
    print(e.reason)

