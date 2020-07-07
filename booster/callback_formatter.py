#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    格式器用于格式化数据结构, 回调格式器
written by pyleo.
"""


class CallBackFormatter:
    """回调格式器

    """
    
    def __init__(self):
        self.logger: any = None                     # 日志记录器
    
    def format_as_sync(self) -> dict:
        """格式化同步数据
        :return:  dict
        """
        sync_data = {
            "success": "false",
            "msg": "占舱失败",
            "occupyCabinId": 0,
            "totalPrice": "",
            "currency": "",
            "pnrCode": "",
            "pnrTimeout": "",
            "orderSrc": 1,
            "carrierAccount": "",
            "carrierAccountAgent": "",
            "farePrice": "",
            "fareTax": "",
            "adultPrice": "",
            "adultTax": "",
            "childPrice": "",
            "childTax": "",
            "fromSegments": [],
            "baggagePrice": -1,
            "passengerBaggages": []
        }
        self.logger.info("格式同步回调成功(*^__^*)【sync】")
        return sync_data
    
    def format_as_async(self) -> dict:
        """格式化异步数据
        :return:  dict
        """
        async_data = {
            "success": "false",                 # 返回状态
            "msg": "占舱失败",                  # 返回信息
            "occupyCabinId": 0,                 # 任务编号
            "totalPrice": "",                   # 总价
            "currency": "",                     # 货币类型
            "pnrCode": "",                      # 票号
            "pnrTimeout": "",                   # 票号超时时间
            "orderSrc": 1,                      # 是否是企业类型
            "carrierAccount": "",               # 个人账号
            "carrierAccountAgent": "",          # 企业账号
            "baggagePrice": -1,                 # 行李总价
            "passengerBaggages": [],            # 行李参数
        }
        self.logger.info("格式异步回调成功(*^__^*)【async】")
        return async_data
