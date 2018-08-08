import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

postData = {}
sandCookies = {'li': '123'}
r = requests.post('https://www.zhihu.com/', data=postData, headers=headers, cookies=sandCookies)

# print(r.content)
# print(r.encoding)
# print(r.text)
# print(r.headers)
print(r.status_code)

for cookie in r.cookies.items():
    # print(r.cookies.get(cookie))
    print(cookie)
