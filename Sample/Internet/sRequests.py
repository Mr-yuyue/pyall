import requests

r = requests.post('https://www.zhihu.com/')
# print(r.text)
print(r.content)
