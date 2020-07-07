#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    解析器用于解析数据结构, 基础解析器
written by pyleo.
"""
from urllib.parse import urlencode, parse_qs, urlparse
from urllib.parse import quote_plus, unquote_plus
import re
import json
import jsonpath


class BasicParser:
    """基础解析器

    """

    def __init__(self):
        self.logger: any = None  # 日志记录器

    def parse_as_url(self, source_data: tuple = None, url_encoding: str = "utf-8") -> str:
        """解析地址
        :param source_data:  来源数据
        :param url_encoding:  解析编码
        :return:  str
        """
        if not source_data or type(source_data) is not tuple or type(url_encoding) is not str:
            self.logger.info("解析地址非法传参(*>﹏<*)【url】")
            return ""

        return_data = urlencode(source_data, encoding=url_encoding)

        if not return_data:
            self.logger.info("解析地址内容失败(*>﹏<*)【url】")

        return return_data

    def parse_as_params(self, source_url: str = "", url_encoding: str = "utf-8") -> tuple:
        """解析参数
        :param source_url:  来源地址
        :param url_encoding:  解析编码
        :return:  dict
        """
        if not source_url or type(source_url) is not str or type(url_encoding) is not str:
            self.logger.info("解析参数非法传参(*>﹏<*)【params】")
            return ()

        return_list = []
        url_query = urlparse(source_url).query
        url_dict = parse_qs(url_query, encoding=url_encoding)
        for k, v in url_dict.items():
            for i in v:
                return_list.append((k, i))
        return_tuple = tuple(return_list)

        if not return_tuple:
            self.logger.info("解析参数内容失败(*>﹏<*)【params】")

        return return_tuple

    def parse_as_quote(self, source_data: str = "", quote_encoding: str = "utf-8") -> str:
        """解析引用
        :param source_data:  来源数据
        :param quote_encoding:  解析编码
        :return:  str
        """
        if not source_data or type(source_data) is not str or type(quote_encoding) is not str:
            self.logger.info("解析引用非法传参(*>﹏<*)【quote】")
            return ""

        return_data = quote_plus(source_data, encoding=quote_encoding)

        if not return_data:
            self.logger.info("解析引用内容失败(*>﹏<*)【quote】")

        return return_data

    def parse_as_unquote(self, source_data: str = "", quote_encoding: str = "utf-8") -> str:
        """解析反引
        :param source_data:  来源数据
        :param quote_encoding:  解析编码
        :return:  str
        """
        if not source_data or type(source_data) is not str or type(quote_encoding) is not str:
            self.logger.info("解析反引非法传参(*>﹏<*)【unquote】")
            return ""

        return_data = unquote_plus(source_data, encoding=quote_encoding)

        if not return_data:
            self.logger.info("解析反引内容失败(*>﹏<*)【unquote】")

        return return_data

    def parse_as_list(self, source_data: any = None, list_encoding: str = "utf-8") -> list:
        """解析列表
        :param source_data:  来源数据type(str/bytes)
        :param list_encoding:  解析编码
        :return:  list
        """
        try:
            return_data = json.loads(source_data, encoding=list_encoding)
        except Exception as ex:
            self.logger.info("解析列表内容失败(*>﹏<*)【list】")
            self.logger.info(f"解析列表失败原因(*>﹏<*)【{ex}】")
            return []
        else:
            if type(return_data) is not list:
                self.logger.info("解析列表非法返回(*>﹏<*)【list】")
                return []

            if not return_data:
                self.logger.info("解析列表内容失败(*>﹏<*)【list】")

            return return_data

    def parse_as_dict(self, source_data: any = None, dict_encoding: str = "utf-8") -> dict:
        """解析字典
        :param source_data:  来源数据type(str/bytes)
        :param dict_encoding:  解析编码
        :return:  list
        """
        try:
            return_data = json.loads(source_data, encoding=dict_encoding)
        except Exception as ex:
            self.logger.info("解析字典内容失败(*>﹏<*)【dict】")
            self.logger.info(f"解析字典失败原因(*>﹏<*)【{ex}】")
            return {}
        else:
            if type(return_data) is not dict:
                self.logger.info("解析列表非法返回(*>﹏<*)【dict】")
                return {}

            if not return_data:
                self.logger.info("解析字典内容失败(*>﹏<*)【dict】")

            return return_data

    def parse_as_json(self, source_data: any = None, json_encoding: str = "utf-8") -> str:
        """解析字符
        :param source_data:  来源数据
        :param json_encoding:  解析编码
        :return:  str
        """
        if not source_data or type(json_encoding) is not str:
            self.logger.info("解析字符非法传参(*>﹏<*)【json】")
            return ""

        return_data = json.dumps(source_data, encoding=json_encoding)

        if not return_data:
            self.logger.info("解析字符内容失败(*>﹏<*)【json】")

        return return_data

    def parse_as_sub(self, replace_syntax: str = "", replaced_string: str = "", source_data: str = "") -> str:
        """解析替换
        :param replace_syntax:  正则语法
        :param replaced_string:  替换后字符串
        :param source_data:  来源数据
        :return:  str
        """
        if not replace_syntax or type(replace_syntax) is not str or \
                type(replaced_string) is not str or not source_data or type(source_data) is not str:
            self.logger.info(f"解析替换非法传参(*>﹏<*)【{replace_syntax}】")
            return ""

        return_data = re.sub(replace_syntax, replaced_string, source_data)

        if not return_data:
            self.logger.info(f"解析替换内容失败(*>﹏<*)【{replace_syntax}】")

        return return_data

    def parse_as_clear(self, source_data: str = "") -> str:
        """解析清空
        :param source_data:  来源数据
        :return:  str
        """
        if not source_data or type(source_data) is not str:
            self.logger.info("解析清空非法传参(*>﹏<*)【clear】")
            return ""

        return_data = re.sub("\r|\n|\t|\s+", "", source_data)

        if not return_data:
            self.logger.info("解析清空内容失败(*>﹏<*)【clear】")

        return return_data

    def parse_as_separate(self, source_data: str = "") -> str:
        """解析分割
        :param source_data:  来源数据
        :return:  str
        """
        if not source_data or type(source_data) is not str:
            self.logger.info("解析分割非法传参(*>﹏<*)【separate】")
            return ""

        return_data = re.sub("\r|\n|\t", "", source_data)
        return_data = re.sub("\s+", " ", return_data)
        return_data = return_data.strip(" ")

        if not return_data:
            self.logger.info("解析分割内容失败(*>﹏<*)【separate】")

        return return_data

    def parse_as_regex(self, regex_syntax: str = "", source_data: str = "") -> tuple:
        """解析匹配
        :param regex_syntax: 正则语法
        :param source_data:  来源数据
        :return:  tuple
        """
        if not regex_syntax or type(regex_syntax) is not str \
                or not source_data or type(source_data) is not str:
            self.logger.info(f"解析匹配非法传参(*>﹏<*)【{regex_syntax}】")
            return "", []

        return_data = re.findall(regex_syntax, source_data, re.S)

        if not return_data:
            self.logger.info(f"解析匹配内容失败(*>﹏<*)【{regex_syntax}】")
            return "", []

        return return_data[0], return_data

    def parse_as_path(self, path_syntax: str = "", source_data: any = None) -> tuple:
        """解析路径
        :param path_syntax: 路径语法
        :param source_data:  来源数据
        :return:  any
        """
        if not path_syntax or type(path_syntax) is not str or not source_data:
            self.logger.info(f"解析路径非法传参(*>﹏<*)【{path_syntax}】")
            return "", []

        return_data = jsonpath.jsonpath(source_data, path_syntax)

        if not return_data:
            self.logger.info(f"解析路径内容失败(*>﹏<*)【{path_syntax}】")
            return "", []

        return return_data[0], return_data
