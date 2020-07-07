#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
    written by pyleo
"""
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.common.exceptions import WebDriverException
from urllib3.exceptions import ReadTimeoutError


class Browser:
    """
        谷歌浏览器基础类
    """
    
    def __init__(self) -> None:
        
        self.opts = webdriver.ChromeOptions()
        self.driver = None  # 全局驱动
    
    def set_chrome(self):
        """
        启动谷歌浏览器
        :return: None
        """
        try:
            self.opts.add_argument(
                'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
            self.opts.add_experimental_option('excludeSwitches', ['enable-automation'])
            # self.driver = webdriver.Chrome(executable_path='Chrome/Application/chromedriver.exe', options=self.opts)
            self.driver = webdriver.Chrome(options=self.opts)
            # self.driver.set_page_load_timeout(10)
            # self.driver.set_script_timeout(10)
        except WebDriverException:
            return "启动谷歌程序失败"
        except ReadTimeoutError:
            return "启动谷歌程序超时"
        except Exception as ex:
            return f"{ex}"
        else:
            return "启动谷歌程序成功"
    
    def set_cookies(self, cookies=None):
        """
        设置缓存是否成功
        :param cookies: [{"name": "xx", "value": "xx"}]
        :return: bool
        """
        try:
            self.driver.delete_all_cookies()
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except WebDriverException:
            return "设置缓存程序失败"
        except ReadTimeoutError:
            return "设置缓存程序超时"
        except Exception as ex:
            return f"{ex}"
        else:
            return "设置缓存程序成功"
    
    def set_quit(self):
        """
        关闭会话是否成功
        :return: bool
        """
        try:
            self.driver.quit()
        except WebDriverException:
            return "关闭谷歌程序失败"
        except ReadTimeoutError:
            return "关闭谷歌程序超时"
        except Exception as ex:
            return f"{ex}"
        else:
            return "关闭谷歌程序成功"
    
    def set_url(self, url: str = ""):
        """
        打开页面是否成功
        :param url: 链接地址
        :return: bool
        """
        try:
            self.driver.get(url)
        except WebDriverException:
            return "打开页面程序失败"
        except ReadTimeoutError:
            return "打开页面程序超时"
        except Exception as ex:
            return f"{ex}"
        else:
            return "打开页面程序成功"
    
    def execute_script(self, js: str = ""):
        """
        执行脚本是否成功
        :param timeout: 超时时间
        :param js: 执行脚本["document.getElementById"]
        :return: bool
        """
        try:
            self.driver.execute_script(js)
        except WebDriverException:
            return "执行脚本程序失败"
        except ReadTimeoutError:
            return "执行脚本程序超时"
        except Exception as ex:
            return f"{ex}"
        else:
            return "执行脚本程序成功"
    
    def refresh_page(self):
        """
        选择元素是否成功
        :param css: css语法
        :param value: value值
        :return: None
        """
        try:
            self.driver.refresh()
        except WebDriverException:
            return "刷新页面程序失败"
        except ReadTimeoutError:
            return "刷新页面程序超时"
        except Exception as ex:
            return f"{ex}"
        else:
            return "刷新页面程序成功"
