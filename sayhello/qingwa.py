# -*- coding: UTF-8 -*-

import math
import random
import re

sep = [char for char in "~!@#$%^&*(){}"]
trans = [char for char in "`1234567890[]',.pyfgcrl/=\\aoeuidthns-;qjkxbmwvz\"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ"]
import sys

#分隔符 单字
#sep = [' ']
#字体 单字
#trans = ['咕','呱']
trans_m = {trans[a]:a for a in range(0,len(trans))}

def encrypt_string(message):
    encode_result = ""
    for char in message:
        char_int = ord(char)
        encode_result += tenToAny(len(trans), char_int) + random.choice(sep)

    return encode_result

def decrypt_string(message):
    decode_result = ""

    # 将message转换为list
    rrr = "\\" + "|\\".join(sep)
    message_list = re.split(rrr, message)
    if "" in message_list:
        message_list.remove("")  # 移除list中的空元素

    for i in message_list:
        decode_result += chr(anyToTen(len(trans), i))

    return decode_result

# 将一个m进制的数转换为一个n进制的数
def transfer(m, n, origin):
    num = anyToTen(m, origin)
    target = tenToAny(n, num)
    print(target)


def anyToTen(m, origin):
    # 任意进制的数转换为10机制
    # 先将m转换为10进制
    # 公式 num = an * m**(n-1) + an-1 * m**(n-2).....+ a0 * m**0
    # 直接利用int的自带功能
    sub = 0
    for i,v in enumerate(origin):
        # 权
        p = len(origin) -1 -i
        d = trans_m[v]

        if d != 0:
            sub += int(d*math.pow(m, p))
    return sub


def tenToAny(n, origin):
    # 10进制转换为任意进制的数
    list = []
    while True:
        # 取商
        s = origin // n
        # 取余数
        tmp = origin % n
        list.append(trans[tmp])
        if s == 0:
            break
        origin = s
    list.reverse()
    list = [str(each) for each in list]
    return ''.join(list)

if __name__ == '__main__':
    inppp = input("请输入蛙语或人语：\n")

    if inppp is None or len(inppp) == 0:
        print("空输入")
        exit()

    inppp = inppp.strip()
    if len(inppp) == 0:
        print("空输入")
        exit()

    if inppp[0] in trans_m:
        print(decrypt_string(inppp))
    else:
        print(encrypt_string(inppp))
