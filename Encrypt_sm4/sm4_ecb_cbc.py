#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 14:29
# @Author  : 刘华兴
# @Site    : 
# @File    : Encrypt_sm4.py
#@time: 2019/10/24 14:29
# @Software: PyCharm
import os
import hashlib
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT

my_md5 = hashlib.md5()
my_md5.update("pku".encode('utf-8'))
key = bytes(my_md5.hexdigest(), encoding='utf-8')
my_md5.update("sspku".encode('utf-8'))
iv = bytes(my_md5.hexdigest(), encoding='utf-8')
# str1为文件名
def sm4_ecb_mode(str1):
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key, SM4_ENCRYPT)
    with open("./pku_logo.rgb", 'rb') as f:
        logo_data = f.read()
        # print(type(logo_data))
        encrypt_logo = crypt_sm4.crypt_ecb(logo_data)
        f.close()
    with open(str1, 'wb') as f:
        f.write(encrypt_logo)
        f.close()

def sm4_cbc_mode(str1):
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key, SM4_ENCRYPT)
    with open("./pku_logo.rgb", 'rb') as f:
        logo_data = f.read()
        # print(logo_data)
        # print((logo_data))
        encrypt_logo = crypt_sm4.crypt_cbc(iv, logo_data)
        # print(encrypt_logo)
        f.close()
    with open(str1, 'wb') as f:
        f.write(encrypt_logo)
        f.close()

if __name__ == '__main__':

    os.system('magick convert pku_logo.png pku_logo.rgb')
    sm4_ecb_mode('sm4ecb.rgb')
    os.system("magick -size 500x314 -depth 8 sm4ecb.rgb sm4ecb.png") # 这里的大小需要根据pku_logo.png的大小来设置
    sm4_cbc_mode('sm4cbc.rgb')
    os.system("magick -size 500x314 -depth 8 sm4cbc.rgb sm4cbc.png")
