#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Tue Jul 09 05:58:50 UTC+8:00 2019
    建造器用于建造请求头, request建造器
written by pyLeo.
"""
import random


class RequestBuilder:
    """request建造器

    """

    def __init__(self):
        self.logger: any = None  # 日志记录器
        # 默认请求头的匹配
        self._default_version: dict = {
            "Chrome": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                          "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Language": "zh-CN,zh;q=0.9"
            },
            "UBrowser": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8"
            },
            "QQBrowser": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3620.400",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9"
            },
            "Firefox": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
            },
            "Firefox32": {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
            },
            "Opera": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9",
            }
        }

    def build_as_header(self, version: str = "Firefox") -> dict:
        """建立基本请求头，默认Chrome, 匹配不到就随机
        :param version:  填入的版本，首字母大写Chrome/Firefox/IE
        :return:  dict
        """
        base_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
        }

        if not version or type(version) is not str:
            self.logger.info(f"建造头部非法传参(*>﹏<*)【{version}】")
            return base_header

        version_dict = self._default_version.get(version)
        if version_dict:
            accept = version_dict.get('Accept')
            user_agent = version_dict.get('User-Agent')
            language = version_dict.get('Accept-Language')
        else:
            key = random.sample(self._default_version.keys(), 1)
            version = key[0]
            version_dict = self._default_version.get(version)
            accept = version_dict.get('Accept')
            user_agent = version_dict.get('User-Agent')
            language = version_dict.get('Accept-Language')
        if user_agent and language:
            base_header['Accept'] = accept
            base_header['User-Agent'] = user_agent
            base_header['Accept-Language'] = language

        self.logger.info(f"建造头部版本成功(*^__^*)【{version}】")
        return base_header
