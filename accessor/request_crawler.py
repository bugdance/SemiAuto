#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Tue Jul 09 05:58:50 UTC+8:00 2019
    爬行器用于交互数据, request爬行器
written by pyleo.
"""
from requests import session
from requests.utils import dict_from_cookiejar
from requests.adapters import HTTPAdapter
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


class RequestCrawler:
    """request爬行器

    """

    def __init__(self):
        disable_warnings(InsecureRequestWarning)    # 消除ssl报警
        self.logger: any = None                     # 日志记录器
        self.session: any = session()               # 全局会话
        self.retry_count: int = 2                   # 请求重试次数
        self.url: str = ""                          # 请求地址
        self.header: dict = {}                      # 请求头
        self.param_data: tuple = ()                 # 请求参数数据
        self.post_data: list = []                   # 请求主体数据
        self.timeout: int = 25                      # 请求超时时间
        self.page_source: any = None                # 页面源代码

    def set_to_cookies(self, cookie_list: list = None) -> bool:
        """设置用户缓存
        :param cookie_list:  要设置的缓存字典,name/value/domain/path
        :return:  bool
        """
        try:
            for cookie_dict in cookie_list:
                cookie_name = cookie_dict.get('name')
                cookie_value = cookie_dict.get('value')
                # cookie_domain = cookie_dict.get('domain')
                # cookie_path = cookie_dict.get('path')
                self.session.cookies.set(
                    name=cookie_name, value=cookie_value)
        except Exception as ex:
            self.logger.info(f"设置用户缓存失败(*>﹏<*)【{cookie_list}】")
            self.logger.info(f"设置缓存失败原因(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"设置用户缓存成功(*^__^*)【{cookie_list}】")
            return True

    def set_to_cookie(self, cookie_dict: dict = None) -> bool:
        """设置用户缓存
        :param cookie_dict:  要设置的缓存字典,name/value/domain/path
        :return:  bool
        """
        try:
            for k, v in cookie_dict.items():
                self.session.cookies.set(
                    name=k, value=v)
        except Exception as ex:
            self.logger.info(f"设置用户缓存失败(*>﹏<*)【{cookie_dict}】")
            self.logger.info(f"设置缓存失败原因(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"设置用户缓存成功(*^__^*)【{cookie_dict}】")
            return True

    def get_from_cookies(self) -> dict:
        """获取用户缓存
        :return:  dict
        """
        return dict_from_cookiejar(self.session.cookies)

    def set_to_configs(self):
        """基本配置设置
        :return:  bool
        """
        self.session.verify = False
        self.session.max_redirects = 1
        # self.session.mount('http://', HTTPAdapter(max_retries=self.retry_count))
        # self.session.mount('https://', HTTPAdapter(max_retries=self.retry_count))
        # self.session.max_redirects = 2

    def set_to_proxy(self, enable_proxy: bool = False, address: str = "") -> bool:
        """设置请求代理
        :param enable_proxy:  是否使用代理
        :param address:  代理地址 type(http://1.1.1.1:22443 or http://yunku:123@1.1.1.1:3138)
        :return:  bool
        """
        if type(enable_proxy) is not bool or type(address) is not str:
            self.logger.info(f"设置代理非法传参(*>﹏<*)【{enable_proxy}】【{address}】")
            return False
        if enable_proxy:
            self.session.proxies.update({"https": address, "http": address})
        else:
            self.session.proxies.update({})

        self.logger.info(f"设置请求代理成功(*^__^*)【{address}】")
        return True

    def request_to_get(self, page_type: str = "text", status_code: int = 200,
                       redirect: bool = False, page_encoding: str = "utf-8") -> bool:
        """GET请求
        :param page_type:  指定响应数据类型 type(text/content/json)
        :param status_code:  指定响应编码，默认200 type(200/302)
        :param redirect:  指定响应是否跳转, 默认不跳转
        :param page_encoding:  响应页面数据的编码 type(utf-8/iso-8859-1)
        :return:  bool
        """
        try:
            response = self.session.get(
                url=self.url, headers=self.header, params=self.param_data,
                allow_redirects=redirect, timeout=self.timeout)
            response.encoding = page_encoding
        except Exception as ex:
            self.logger.info(f"请求超时或者失败(*>﹏<*)【GET】【{self.url}】")
            self.logger.info(f"超时或者失败原因(*>﹏<*)【{ex}】")
            return False
        else:
            if self.response_as_page(page_type, status_code, response):
                return True
            else:
                return False

    def request_to_delete(self, data_type: str = "data", page_type: str = "text",
                          status_code: int = 200, redirect: bool = False,
                          page_encoding: str = "utf-8") -> bool:
        """POST请求
        :param data_type:  发送请求数据的类型 type(data/json/files)
        :param page_type:  指定响应数据类型 type(text/content/json)
        :param status_code:  指定响应编码，默认200 type(200/302)
        :param redirect:  指定响应是否跳转, 默认不跳转
        :param page_encoding:  响应页面数据的编码 type(utf-8/iso-8859-1)
        :return:  bool
        """
        try:
            if data_type == "data":
                response = self.session.delete(
                    url=self.url, headers=self.header, params=self.param_data,
                    data=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            elif data_type == "json":
                response = self.session.delete(
                    url=self.url, headers=self.header, params=self.param_data,
                    json=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            elif data_type == "files":
                response = self.session.delete(
                    url=self.url, headers=self.header, params=self.param_data,
                    files=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            else:
                self.logger.info(f"请求非法传参类型(*>﹏<*)【{data_type}】【{self.url}】")
                return False
            response.encoding = page_encoding
        except Exception as ex:
            self.logger.info(f"请求超时或者失败(*>﹏<*)【POST】【{self.url}】")
            self.logger.info(f"超时或者失败原因(*>﹏<*)【{ex}】")
            return False
        else:
            if self.response_as_page(page_type, status_code, response):
                return True
            else:
                return False

    def request_to_post(self, data_type: str = "data", page_type: str = "text",
                        status_code: int = 200, redirect: bool = False,
                        page_encoding: str = "utf-8") -> bool:
        """POST请求
        :param data_type:  发送请求数据的类型 type(data/json/files)
        :param page_type:  指定响应数据类型 type(text/content/json)
        :param status_code:  指定响应编码，默认200 type(200/302)
        :param redirect:  指定响应是否跳转, 默认不跳转
        :param page_encoding:  响应页面数据的编码 type(utf-8/iso-8859-1)
        :return:  bool
        """
        try:
            if data_type == "data":
                response = self.session.post(
                    url=self.url, headers=self.header, params=self.param_data,
                    data=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            elif data_type == "json":
                response = self.session.post(
                    url=self.url, headers=self.header, params=self.param_data,
                    json=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            elif data_type == "files":
                response = self.session.post(
                    url=self.url, headers=self.header, params=self.param_data,
                    files=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            else:
                self.logger.info(f"请求非法传参类型(*>﹏<*)【{data_type}】【{self.url}】")
                return False
            response.encoding = page_encoding
        except Exception as ex:
            self.logger.info(f"请求超时或者失败(*>﹏<*)【POST】【{self.url}】")
            self.logger.info(f"超时或者失败原因(*>﹏<*)【{ex}】")
            return False
        else:
            if self.response_as_page(page_type, status_code, response):
                return True
            else:
                return False

    def request_to_put(self, data_type: str = "data", page_type: str = "text",
                       status_code: int = 200, redirect: bool = False,
                       page_encoding: str = "utf-8") -> bool:
        """PUT请求
        :param data_type:  发送请求数据的类型 type(data/json/files)
        :param page_type:  指定响应数据类型 type(text/content/json)
        :param status_code:  指定响应编码，默认200 type(200/302)
        :param redirect:  指定响应是否跳转, 默认不跳转
        :param page_encoding:  响应页面数据的编码 type(utf-8/iso-8859-1)
        :return:  bool
        """
        try:
            if data_type == "data":
                response = self.session.put(
                    url=self.url, headers=self.header, params=self.param_data,
                    data=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            elif data_type == "json":
                response = self.session.put(
                    url=self.url, headers=self.header, params=self.param_data,
                    json=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            elif data_type == "files":
                response = self.session.put(
                    url=self.url, headers=self.header, params=self.param_data,
                    files=self.post_data, allow_redirects=redirect, timeout=self.timeout)
            else:
                self.logger.info(f"请求非法传参类型(*>﹏<*)【{data_type}】【{self.url}】")
                return False
            response.encoding = page_encoding
        except Exception as ex:
            self.logger.info(f"请求超时或者失败(*>﹏<*)【PUT】【{self.url}】")
            self.logger.info(f"超时或者失败原因(*>﹏<*)【{ex}】")
            return False
        else:
            if self.response_as_page(page_type, status_code, response):
                return True
            else:
                return False

    def response_as_page(self, page_type: str = "text", status_code: int = 200, response: any = None) -> bool:
        """指定响应返回
        :param page_type:  指定响应数据类型 type(text/content/json)
        :param status_code:  指定响应编码，默认200 type(200/302)
        :param response:  指定响应
        :return:  bool
        """
        try:
            if status_code != response.status_code:
                self.logger.info(f"返回页面非法编码(*>﹏<*)【指定{status_code}】【返回{response.status_code}】【{self.url}】")
                # self.logger.info(response.text)
            if page_type == "content":
                self.page_source = response.content
            elif page_type == "text":
                self.page_source = response.text
            elif page_type == "json":
                self.page_source = response.json()
            else:
                response.close()
                self.logger.info(f"返回非法传参类型(*>﹏<*)【{page_type}】【{self.url}】")
                return False
        except Exception as ex:
            response.close()
            self.logger.info(f"返回页面解析失败(*>﹏<*)【{self.url}】")
            self.logger.info(f"返回页面失败原因(*>﹏<*)【{ex}】")
            return False
        else:
            response.close()
            self.logger.info(f"返回页面解析成功(*^__^*)【{status_code}】【{self.url}】")
            return True


