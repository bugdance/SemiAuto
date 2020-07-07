#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    测试单元
written by pyleo.
"""
import logging
from accessor.request_builder import RequestBuilder
from accessor.request_crawler import RequestCrawler
from booster.basic_parser import BasicParser
from booster.date_formatter import DateFormatter
from booster.dom_parser import DomParser
from hammer.data_tester import a

from accessor.selenium_crawler import SeleniumCrawler


logger = logging.getLogger("test")
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('[%(asctime)s]%(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


if __name__ == '__main__':
    RB = RequestBuilder()
    RC = RequestCrawler()
    BP = BasicParser()
    DF = DateFormatter()
    DP = DomParser()
    SC = SeleniumCrawler()
    RB.logger = logger
    RC.logger = logger
    BP.logger = logger
    DF.logger = logger
    DP.logger = logger
    SC.logger = logger

    SC.set_as_chrome()
    SC.get_from_url("https://www.baidu.com")
    # print(SC.get_from_cookies())
    a = {'sRpK8nqm_sc': 'AnsWvW1uAQAA0STsazxYkSEgDE0Yf_f8jkKMD7SoD9lwlZRCrAAAAW5tvRZ7AVCtV3U|1|1|836fa75e9970cec90e8f4e02563ca76fb3c93fdc', 'U08jgd0C': 'AtMovW1uAQAA1jgXFFIKqb-seIimGjYrydWxwnD4BCtDsMEr0QAAAW5tvSjTAf1wldo=', 'akavpau_prod_fullsite': '1573799173~id=57235b03bd9fd64a386979e6dba23367'}

    SC.set_as_cookies("southwest.com", a)
    SC.get_from_url("https://www.southwest.com/air/booking/purchase.html")
