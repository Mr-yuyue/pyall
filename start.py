# -*- coding: utf-8 -*-

# try:
#     f = open('测试文本读取', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

with open('测试文本读取', 'r', encoding='GBK', errors="ignore") as f:
    print(f.read())
