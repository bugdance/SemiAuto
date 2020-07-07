#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019

written by pyleo.
"""


LOGIN_URL = "http://flight.yeebooking.com/fii/semi-automatic/order-list"
LOCK_URL = "http://flight.yeebooking.com/fii/semi-automatic/ticket"
TIME_COUNT = 5

ORDER_COMPANY = ["MM", "VY", "U2"]
SCRAMBLE_COMPANY = ["MM"]

ORDER_STATUS = {
    "1": "生单成功待支付",
    "2": "支付成功等待出票",
    "3": "订单取消",
    "4": "出票完成",
    "5": "退款成功"
}

ORDER_URL = {
    "MM": "http://116.62.51.105:18081/mm_orders/",
    "VY": "http://116.62.51.105:18081/vy_orders/",
    "U2": "http://116.62.51.105:18081/u2_orders/",
}

ORDER_PAY = {
    "MM": ['booking.flypeach.com', "https://booking.flypeach.com/cn/pay"],
    "VY": ["tickets.vueling.com", "https://tickets.vueling.com/Payment.aspx"],
    "U2": [".easyjet.com", "https://www.easyjet.com/en/buy/payment"]
}
