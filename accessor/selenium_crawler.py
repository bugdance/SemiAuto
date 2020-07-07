#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Tue Jul 09 05:58:50 UTC+8:00 2019
    爬行器用于交互数据, request爬行器
written by pyLeo.
"""
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from urllib3.exceptions import ReadTimeoutError
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import os


class SeleniumCrawler:
    """request爬行器

    """
    def __init__(self):
        self.fox_prof = webdriver.FirefoxProfile()          # 火狐配置
        self.fox_ops = webdriver.FirefoxOptions()           # 火狐选项
        self.fox_caps = None
        self.chrome_ops = webdriver.ChromeOptions()         # 谷歌选项
        self.chrome_caps = None
        self.driver = None
        self.logger = None

    def set_as_firefox(self) -> bool:
        """启动无头是否成功
        :return: bool
        """
        self.fox_ops.headless = False
        # self.prof.set_preference('network.proxy.type', 1)
        # self.prof.set_preference('network.proxy.receive', "121.20.108.88")
        # self.prof.set_preference('network.proxy.http_port', 3138)
        # self.prof.set_preference('network.proxy.ssl', "121.20.108.88")
        # self.prof.set_preference('network.proxy.ssl_port', 3138)
        # self.fox_prof.set_preference('permissions.default.image', 2)  # 禁止加载图片
        # self.fox_prof.set_preference(
        #     "general.useragent.override",
        #     "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0")
        self.fox_prof.accept_untrusted_certs = True
        self.fox_prof.update_preferences()
        self.fox_caps = self.fox_ops.to_capabilities()
        try:
            self.driver = webdriver.Firefox(
                desired_capabilities=self.fox_caps, firefox_profile=self.fox_prof, options=self.fox_ops)
            # self.driver.execute_script(
            #     "Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});")
            self.driver.set_page_load_timeout(10)           # 全局页面加载超时
            self.driver.set_script_timeout(10)              # 全局js加载超时
        except WebDriverException:
            self.logger.info("启动无头框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("启动无头响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"启动无头未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"启动无头程序成功(*^__^*)【OK】")
            return True

    def set_as_chrome(self) -> bool:
        """启动无头是否成功
        :return: bool
        """
        self.chrome_ops.headless = False
        self.chrome_ops.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36')
        # self.chrome_ops.add_argument('--proxy-server=http://127.0.0.1:8888')
        # self.chrome_ops.add_argument('--no-sandbox')  # 无头下禁用沙盒
        # self.chrome_ops.add_argument('--disable-dev-tools')  # 无头下禁用dev
        # self.chrome_ops.add_argument('--disable-gpu')  # 禁用gpu加速
        # self.chrome_ops.add_argument('--disable-infobars')  # 禁用提示
        # self.chrome_ops.add_argument('--ignore-certificate-errors')  # 忽略证书错误
        # self.chrome_ops.add_argument('--allow-running-insecure-content')  # 与上同步使用
        # self.chrome_ops.add_argument('--disable-crash-reporter')  # 禁用汇报
        # self.chrome_ops.add_argument('--incognito')  # 隐身模式
        # preferences = {'profile.default_content_setting_values':
        #                    {'images': 2, 'notifications': 2,}}
        # self.chrome_ops.add_experimental_option('prefs', preferences)
        self.chrome_ops.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_caps = self.chrome_ops.to_capabilities()

        # chrome_ops.add_experimental_option('w3c', False)
        # chrome_caps = chrome_ops.to_capabilities()
        # chrome_caps['loggingPrefs'] = {'performance': 'ALL'}
        # log = driver.get_log("performance")
        
        try:
            self.driver = webdriver.Chrome(options=self.chrome_ops, desired_capabilities=self.chrome_caps)
            # self.driver.set_page_load_timeout(10)
            # self.driver.set_script_timeout(5)
        except WebDriverException:
            self.logger.info("启动无头框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("启动无头响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"启动无头未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"启动无头程序成功(*^__^*)【OK】")
            return True
    
    def set_to_quit(self) -> bool:
        """关闭无头是否成功
        :return: bool
        """
        try:
            self.driver.quit()
        except WebDriverException:
            self.logger.info("关闭无头框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("关闭无头响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"关闭无头未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info("关闭无头程序成功(*^__^*)【OK】")
            return True
    
    def set_to_close(self) -> bool:
        """关闭窗口是否成功
        :return: bool
        """
        try:
            self.driver.close()
        except WebDriverException:
            self.logger.info("关闭窗口框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("关闭窗口响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"关闭窗口未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info("关闭窗口程序成功(*^__^*)【OK】")
            return True
    
    def get_from_log(self) -> list:
        """获取日志是否成功
        :return: list
        """
        try:
            log = self.driver.get_log("performance")
        except WebDriverException:
            self.logger.info("获取日志框架失败(*>﹏<*)【NO】")
            return []
        except ReadTimeoutError:
            self.logger.info("获取日志响应超时(⊙﹏⊙)【NO】")
            return []
        except Exception as ex:
            self.logger.info(f"获取日志未知失败(*>﹏<*)【{ex}】")
            return []
        else:
            self.logger.info("获取日志程序成功(*^__^*)【OK】")
            return log
    
    def set_to_refresh(self) -> bool:
        """刷新页面是否成功
        :return: bool
        """
        try:
            self.driver.refresh()
        except WebDriverException:
            self.logger.info("刷新页面框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("刷新页面响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"刷新页面未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info("刷新页面程序成功(*^__^*)【OK】")
            return True
    
    def set_as_script(self, js: str = "") -> bool:
        """执行脚本是否成功
        :param js: 执行脚本类似document.getElementById
        :return: bool
        """
        try:
            self.driver.execute_script(js)
        except WebDriverException:
            self.logger.info("执行脚本框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("执行脚本响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"执行脚本未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info("执行脚本程序成功(*^__^*)【OK】")
            return True
    
    def get_from_url(self, url: str = "") -> bool:
        """ 打开页面是否成功
        :param url: 链接地址
        :return: bool
        """
        try:
            self.driver.get(url)
        except WebDriverException:
            self.logger.info(f"打开页面框架失败(*>﹏<*)【{url}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"打开页面响应超时(⊙﹏⊙)【{url}】")
            return False
        except Exception as ex:
            self.logger.info(f"打开页面未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"打开页面程序成功(*^__^*)【{url}】")
            return True

    def get_from_page(self) -> str:
        """获取页面是否成功
        :return: str
        """
        try:
            page = self.driver.page_source
        except WebDriverException:
            self.logger.info("获取页面框架失败(*>﹏<*)【NO】")
            return ""
        except ReadTimeoutError:
            self.logger.info("获取页面响应超时(⊙﹏⊙)【NO】")
            return ""
        except Exception as ex:
            self.logger.info(f"获取页面未知失败(*>﹏<*)【{ex}】")
            return ""
        else:
            self.logger.info("获取页面程序成功(*^__^*)【OK】")
            return page

    def set_to_delete(self) -> bool:
        """删除缓存是否成功
        :return: bool
        """
        try:
            self.driver.delete_all_cookies()
        except WebDriverException:
            self.logger.info("删除缓存框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("删除缓存响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"删除缓存未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info("删除缓存程序成功(*^__^*)【OK】")
            return True

    def get_from_cookies(self) -> list:
        """获取缓存是否成功
        :return: list
        """
        try:
            cookies = self.driver.get_cookies()
        except WebDriverException:
            self.logger.info("获取缓存框架失败(*>﹏<*)【NO】")
            return []
        except ReadTimeoutError:
            self.logger.info("获取缓存响应超时(⊙﹏⊙)【NO】")
            return []
        except Exception as ex:
            self.logger.info(f"获取缓存未知失败(*>﹏<*)【{ex}】")
            return []
        else:
            self.logger.info("获取缓存程序成功(*^__^*)【OK】")
            return cookies
    
    def set_as_cookies(self, domain: str = "", cookie_dict: dict = None) -> bool:
        """设置缓存是否成功
        :param domain: 域名
        :param cookie_dict: 接口传来的cookie
        :return: bool
        """
        try:
            self.driver.delete_all_cookies()
            for i, v in cookie_dict.items():
                self.driver.add_cookie({'name': i, 'value': v, 'domain': domain, 'path': '/'})
        except WebDriverException:
            self.logger.info("设置缓存框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("设置缓存响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"设置缓存未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info("设置缓存程序成功(*^__^*)【OK】")
            return True
        
    def get_from_window(self) -> str:
        """获取窗口是否成功
        :return: str
        """
        try:
            window = self.driver.current_window_handle
        except WebDriverException:
            self.logger.info("获取窗口框架失败(*>﹏<*)【NO】")
            return ""
        except ReadTimeoutError:
            self.logger.info("获取窗口响应超时(⊙﹏⊙)【NO】")
            return ""
        except Exception as ex:
            self.logger.info(f"获取窗口未知失败(*>﹏<*)【{ex}】")
            return ""
        else:
            self.logger.info("获取窗口程序成功(*^__^*)【OK】")
            return window
        
    def set_to_back(self, window: str = "") -> bool:
        """切换窗口是否成功
        :param window: 窗口id
        :return: bool
        """
        try:
            self.driver.switch_to.window(window)
        except WebDriverException:
            self.logger.info("切换窗口框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("切换窗口响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"切换窗口未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info("切换窗口程序成功(*^__^*)【OK】")
            return True
    
    def set_to_switch(self, *window) -> bool:
        """返回窗口是否成功
        :param window: 窗口ID，可多个参数
        :return: bool
        """
        try:
            handles = self.driver.window_handles
            for handle in window:
                handles.remove(handle)
            self.driver.switch_to.window(handles[0])
        except WebDriverException:
            self.logger.info("返回窗口框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("返回窗口响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"返回窗口未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info("返回窗口程序成功(*^__^*)【OK】")
            return True
    
    def set_to_be(self, url: str = "", seconds: float = 1) -> bool:
        """等待元素是否成功
        :param url: css语法
        :param seconds: 超时时间
        :return: bool
        """
        try:
            WebDriverWait(driver=self.driver, timeout=seconds, poll_frequency=0.1).until(
                EC.url_to_be(url))
        except WebDriverException:
            self.logger.info(f"等待元素框架失败(*>﹏<*)【{url}】【{seconds}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"等待元素响应超时(⊙﹏⊙)【{url}】【{seconds}】")
            return False
        except Exception as ex:
            self.logger.info(f"等待元素未知失败(*>﹏<*)【{url}】")
            return False
        else:
            self.logger.info(f"等待元素程序成功(*^__^*)【{url}】【{seconds}】")
            return True
    
    def set_to_find(self, css: str = "", seconds: float = 1) -> bool:
        """发现元素是否成功
        :param css: css语法
        :param seconds: 超时时间
        :return: bool
        """
        try:
            WebDriverWait(driver=self.driver, timeout=seconds, poll_frequency=0.1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        except WebDriverException:
            self.logger.info(f"发现元素框架失败(*>﹏<*)【{css}】【{seconds}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"发现元素响应超时(⊙﹏⊙)【{css}】【{seconds}】")
            return False
        except Exception as ex:
            self.logger.info(f"发现元素未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"发现元素程序成功(*^__^*)【{css}】【{seconds}】")
            return True

    def set_to_wait(self, css: str = "", seconds: float = 1) -> bool:
        """等待元素是否成功
        :param css: css语法
        :param seconds: 超时时间
        :return: bool
        """
        try:
            WebDriverWait(driver=self.driver, timeout=seconds, poll_frequency=0.1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        except WebDriverException:
            self.logger.info(f"等待元素框架失败(*>﹏<*)【{css}】【{seconds}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"等待元素响应超时(⊙﹏⊙)【{css}】【{seconds}】")
            return False
        except Exception as ex:
            self.logger.info(f"等待元素未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"等待元素程序成功(*^__^*)【{css}】【{seconds}】")
            return True

    def set_to_touch(self, css: str = "", seconds: float = 1) -> bool:
        """触碰元素是否成功
        :param css: css语法
        :param seconds: 超时时间
        :return: bool
        """
        try:
            WebDriverWait(driver=self.driver, timeout=seconds, poll_frequency=0.1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
        except WebDriverException:
            self.logger.info(f"触碰元素框架失败(*>﹏<*)【{css}】【{seconds}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"触碰元素响应超时(⊙﹏⊙)【{css}】【{seconds}】")
            return False
        except Exception as ex:
            self.logger.info(f"触碰元素未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"触碰元素程序成功(*^__^*)【{css}】【{seconds}】")
            return True

    def set_to_inside(self, css: str = "", text: str = "", seconds: float = 1) -> bool:
        """包含元素是否成功
        :param css: css语法
        :param text: 文本内容
        :param seconds: 超时时间
        :return: bool
        """
        try:
            WebDriverWait(driver=self.driver, timeout=seconds, poll_frequency=0.1).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, css), text))
        except WebDriverException:
            self.logger.info(f"包含元素框架失败(*>﹏<*)【{css}】【{seconds}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"包含元素响应超时(⊙﹏⊙)【{css}】【{seconds}】")
            return False
        except Exception as ex:
            self.logger.info(f"包含元素未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"包含元素程序成功(*^__^*)【{css}】【{seconds}】")
            return True

    def set_to_text(self, css: str = "", value: str = "") -> bool:
        """设置文本是否成功
        :param css: css语法
        :param value: 文本内容
        :return: bool
        """
        try:
            element = self.driver.find_element_by_css_selector(css)
            element.clear()
            element.send_keys(value)
        except WebDriverException:
            self.logger.info(f"设置文本框架失败(*>﹏<*)【{css}】【{value}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"设置文本响应超时(⊙﹏⊙)【{css}】【{value}】")
            return False
        except Exception as ex:
            self.logger.info(f"设置文本未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"设置文本程序成功(*^__^*)【{css}】【{value}】")
            return True

    def get_from_text(self, css: str = "") -> str:
        """获取文本是否成功
        :param css: css语法
        :return: str
        """
        try:
            element = self.driver.find_element_by_css_selector(css)
            css_text = element.text
        except WebDriverException:
            self.logger.info(f"获取文本框架失败(*>﹏<*)【{css}】")
            return ""
        except ReadTimeoutError:
            self.logger.info(f"获取文本响应超时(⊙﹏⊙)【{css}】")
            return ""
        except Exception as ex:
            self.logger.info(f"获取文本未知失败(*>﹏<*)【{ex}】")
            return ""
        else:
            self.logger.info(f"获取文本程序成功(*^__^*)【{css}】【{css_text}】")
            return css_text

    def get_from_attrib(self, css: str = "", attr: str = "") -> str:
        """获取属性是否成功
        :param css: css语法
        :param attr: 标签属性
        :return: str
        """
        try:
            element = self.driver.find_element_by_css_selector(css)
            value = element.get_attribute(attr)
        except WebDriverException:
            self.logger.info(f"获取属性框架失败(*>﹏<*)【{css}】")
            return ""
        except ReadTimeoutError:
            self.logger.info(f"获取属性响应超时(⊙﹏⊙)【{css}】")
            return ""
        except Exception as ex:
            self.logger.info(f"获取属性未知失败(*>﹏<*)【{ex}】")
            return ""
        else:
            self.logger.info(f"获取属性程序成功(*^__^*)【{css}】")
            return value

    def set_to_click(self, css: str = "") -> bool:
        """点击元素是否成功
        :param css: css语法
        :return: bool
        """
        try:
            element = self.driver.find_element_by_css_selector(css)
            element.click()
        except WebDriverException:
            self.logger.info(f"点击元素框架失败(*>﹏<*)【{css}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"点击元素响应超时(⊙﹏⊙)【{css}】")
            return False
        except Exception as ex:
            self.logger.info(f"点击元素未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"点击元素程序成功(*^__^*)【{css}】")
            return True

    def get_from_alert(self, seconds: float = 1) -> bool:
        """获取弹框是否成功
        :param seconds: 超时时间
        :return: bool
        """
        try:
            WebDriverWait(driver=self.driver, timeout=seconds, poll_frequency=0.1).until(EC.alert_is_present())
        except WebDriverException:
            self.logger.info(f"获取弹框框架失败(*>﹏<*)【{seconds}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"获取弹框响应超时(⊙﹏⊙)【{seconds}】")
            return False
        except Exception as ex:
            self.logger.info(f"获取弹框未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"获取弹框程序成功(*^__^*)【{seconds}】")
            return True

    def set_to_alert(self) -> bool:
        """确认弹框是否成功
        :return: bool
        """
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except WebDriverException:
            self.logger.info("确认弹框框架失败(*>﹏<*)【NO】")
            return False
        except ReadTimeoutError:
            self.logger.info("确认弹框响应超时(⊙﹏⊙)【NO】")
            return False
        except Exception as ex:
            self.logger.info(f"确认弹框未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"确认弹框程序成功(*^__^*)【OK】")
            return True

    def set_to_select(self, css: str = "", value: str = "") -> bool:
        """选择元素是否成功
        :param css: css语法
        :param value: value值
        :return: None
        """
        try:
            element = self.driver.find_element_by_css_selector(css)
            Select(element).select_by_value(value)
        except WebDriverException:
            self.logger.info(f"选择元素框架失败(*>﹏<*)【{css}】")
            return False
        except ReadTimeoutError:
            self.logger.info(f"选择元素响应超时(⊙﹏⊙)【{css}】")
            return False
        except Exception as ex:
            self.logger.info(f"选择元素未知失败(*>﹏<*)【{ex}】")
            return False
        else:
            self.logger.info(f"选择元素程序成功(*^__^*)【{css}】")
            return True

    def set_to_shell(self, shell: str = "") -> bool:
        """执行脚本是否成功
        :param shell: 脚本语法
        :return: bool
        """
        try:
            code = os.system(shell)  # 执行脚本
        except Exception as ex:
            self.logger.info(f"执行脚本程序失败(*>﹏<*)【{ex}】")
            return False
        else:
            if not code:
                self.logger.info(f"执行脚本程序成功(*^__^*)【{code}】")
                return True
            else:
                self.logger.info(f"执行脚本程序失败(*>﹏<*)【{code}】")
                return False






    # def enter_element(self, css) -> bool:
    #     """
    #     回车元素是否成功
    #     :param css: css语法
    #     :return: bool
    #     """
    #     try:
    #         element = self.driver.find_element_by_css_selector(css)
    #         element.send_keys(Keys.ENTER)
    #     except WebDriverException:
    #         self.logger.info(f"回车元素框架失败(*>﹏<*)【{css}】")
    #         return False
    #     except ReadTimeoutError:
    #         self.logger.info(f"回车元素响应超时(⊙﹏⊙)【{css}】")
    #         return False
    #     except Exception as ex:
    #         self.logger.info(f"回车元素未知失败(*>﹏<*)【{ex}】")
    #         return False
    #     else:
    #         self.logger.info(f"回车元素程序成功(*^__^*)【{css}】")
    #         return True

    # def set_style(self, status: str = "", text: str = "", style: str = "") -> None:
    #     """
    #     设置样式是否成功
    #     :param status: 状态是class, id
    #     :param text: 标签
    #     :param style: 样式是none,block
    #     :return: None
    #     """
    #     js = ""
    #     if status == "class":
    #         js = """
    #         var font=document.getElementsByClassName("%s");
    #         for(var i=0;i<font.length;i++){
    #             font[i].style.display='%s';
    #         }
    #         """ % (text, style)
    #     elif status == "id":
    #         js = f'document.getElementById("{text}").style="display: {style};";'
    #     else:
    #         pass

    # def slide_action(self, css: str = "") -> bool:
    #     """
    #     滑块事件
    #     :param css: css语法
    #     :return: None
    #     """
    #     try:
    #         action = ActionChains(self.driver)  # 执行
    #         source = self.driver.find_element_by_css_selector(css)
    #         action.move_to_element(source).click_and_hold(source).perform()  # 移动到滑块
    #         import time
    #         for i in range(5):
    #             action.move_by_offset(xoffset=42, yoffset=0).perform()
    #             # time.sleep(2)
    #         # action.click_and_hold(source).move_by_offset(xoffset=210, yoffset=0)
    #         action.release().perform()  # 执行
    #     except WebDriverException:
    #         self.logger.info(f"滑动元素框架失败(*>﹏<*)【{css}】")
    #         return False
    #     except ReadTimeoutError:
    #         self.logger.info(f"滑动元素响应超时(⊙﹏⊙)【{css}】")
    #         return False
    #     except Exception as ex:
    #         self.logger.info(f"滑动元素未知失败(*>﹏<*)【{ex}】")
    #         return False
    #     else:
    #         self.logger.info(f"滑动元素程序成功(*^__^*)【{css}】")
    #         return True

    # def crop_image(self, css: str = "", path: str = "") -> bool:
    #     """
    #     截取图片是否成功
    #     :param path: 保存地址
    #     :param css: css语法
    #     :return: bool
    #     """
    #     try:
    #         im = Image.open(BytesIO(self.driver.get_screenshot_as_png()))
    #         element = self.driver.find_element_by_css_selector(css)
    #         left = element.location['x']
    #         top = element.location['y']
    #         right = left + element.size['width']
    #         bottom = top + element.size['height']
    #         im = im.crop((left, top, right, bottom))
    #         im.save(path)
    #     except WebDriverException:
    #         self.logger.info(f"截取图片框架失败(*>﹏<*)【{css}】【{path}】")
    #         return False
    #     except ReadTimeoutError:
    #         self.logger.info(f"截取图片响应超时(⊙﹏⊙)【{css}】【{path}】")
    #         return False
    #     except Exception as ex:
    #         self.logger.info(f"截取图片未知失败(*>﹏<*)【{ex}】")
    #         return False
    #     else:
    #         self.logger.info(f"截取图片程序成功(*^__^*)【{css}】【{path}】")
    #         return True
    #
    # def click_image(self, code_list: list, css: str, x_increment: float = 0, y_increment: float = 0) -> bool:
    #     """
    #     点击图片是否成功
    #     :param code_list: 坐标轴数据
    #     :param css: 要点击元素css语法
    #     :param x_increment: x偏移增量
    #     :param y_increment: y偏移增量
    #     :return: bool
    #     """
    #     try:
    #         element = self.driver.find_element_by_css_selector(css)
    #         for i in range(0, len(code_list), 2):
    #             x_move = int(code_list[i]) + x_increment
    #             y_move = int(code_list[i + 1]) + y_increment
    #             ActionChains(self.driver).move_to_element_with_offset(
    #                 element, x_move, y_move).click().perform()
    #     except WebDriverException:
    #         self.logger.info(f"点击图片框架失败(*>﹏<*)【{css}】【{code_list}】")
    #         return False
    #     except ReadTimeoutError:
    #         self.logger.info(f"点击图片响应超时(⊙﹏⊙)【{css}】【{code_list}】")
    #         return False
    #     except Exception as ex:
    #         self.logger.info(f"点击图片未知失败(*>﹏<*)【{ex}】")
    #         return False
    #     else:
    #         self.logger.info(f"点击图片程序成功(*^__^*)【{css}】【{code_list}】")
    #         return True

    # def set_proxy(self, proxy_server: str = "", proxy_auth: str = "") -> None:
    #     """
    #     设置代理是否成功
    #     :return: None
    #     """
    #     if proxy_server and proxy_auth:
    #         self.set_shell("./kill_proxy.sh")
    #         self.set_shell(f'mitmdump -q -p 9000 --mode upstream:{proxy_server} '
    #                        f'--set upstream_auth={proxy_auth} > /dev/null 2>&1 &')
    #         # self.set_shell("kill_proxy.bat")
    #         # self.set_shell(f'start /b mitmdump -p 9000 --mode upstream:{proxy_server} --set upstream_auth={proxy_auth}')
    #         # time.sleep(2)
    #     else:
    #         self.set_shell("./kill_proxy.sh")

