#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    接收器用于接收接口数据并返回响应数据
written by pyleo.
"""
import sys
sys.path.append('..')                           # 导入环境当前目录
from flask import Flask, request, jsonify
import logging
import time
import configparser
import requests


from gainer.occupy_configurer import AIRLINE_COMPANY, OUTLAND_COMPANY, AIRLINE_ACCOUNT
from booster.callback_formatter import CallBackFormatter
from explorer.corpsl_scraper import CorpSLScraper
from explorer.corptr_scraper import CorpTRScraper
from explorer.corpuo_scraper import CorpUOScraper
from explorer.corpxw_scraper import CorpXWScraper
from explorer.pers5j_scraper import Pers5JScraper


# # # app实例
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# # # 日志格式化
app.logger = logging.getLogger('flask')
app.logger.setLevel(level=logging.INFO)
app.formatter = logging.Formatter('[%(asctime)s]%(message)s')
app.handler = logging.FileHandler("occupy.log")
# app.handler = logging.StreamHandler()
app.handler.setFormatter(app.formatter)
app.logger.addHandler(app.handler)


# # # 链接地址,例http://x.x.x.x:18081/occupy/sl/
@app.route('/occupy/<airline_company>/', methods=['POST'])
def occupy(airline_company: str="") -> dict:
    """占舱接口
    :param airline_company:  航司二字码
    :return:  dict
    """
    start_time = time.time()  # 开始计时
    call_back = CallBackFormatter()  # 回调声明
    call_back.logger = app.logger
    return_error = call_back.format_as_sync()  # 返回格式
    # # # 检查各项请求参数
    if not request.get_data():
        msg = f"航司【{airline_company}】占舱请求数据为空"
        return_error['msg'] = msg
        app.logger.info(msg)
        return jsonify(return_error)

    try:
        get_dict = eval(request.get_data())
        order_no = get_dict.get('orderNO')
    except Exception as ex:
        msg = f"航司【{airline_company}】占舱数据格式有误"
        return_error['msg'] = msg
        app.logger.info(msg)
        app.logger.info(ex)
        return jsonify(return_error)
    else:
        if not order_no:
            msg = f"航司【{airline_company}】占舱数据标识为空"
            return_error['msg'] = msg
            app.logger.info(msg)
            return jsonify(return_error)
    
        log_path = "log/{}-{}.log".format(airline_company, order_no)
        # # # 生成全局变量数组，声明变量类
        airline_account = ""
        for k, v in AIRLINE_ACCOUNT.items():
            if k.upper() == airline_company.upper():
                if v.capitalize() == "Corp" or v.capitalize() == "Pers":
                    airline_account = v
                    break
                else:
                    msg = f"航司【{airline_company}】占舱账户类型不对"
                    return_error['msg'] = msg
                    app.logger.info(msg)
                    return jsonify(return_error)
    
        if not airline_account:
            msg = f"航司【{airline_company}】占舱账户标识为空"
            return_error['msg'] = msg
            app.logger.info(msg)
            return jsonify(return_error)
    
        config = configparser.ConfigParser()
        config.read("proxy.ini", encoding="utf-8")
        defaults = config.defaults()
        proxy = defaults.get(airline_company.lower())
        if airline_company in AIRLINE_COMPANY:
            if proxy:
                enable_proxy = True
            else:
                enable_proxy = False
        
            create_var = globals()
            scraper = create_var[airline_account.capitalize() + airline_company.upper() + "Scraper"]()
            result_data = scraper.process_to_main(order_no, log_path, get_dict, enable_proxy, proxy)
            result_msg = result_data.get('msg')
            end_time = (time.time() - start_time).__round__(2)
            msg = f"航司【{airline_company}】占舱请求返回成功【{end_time}】【{order_no}】【{result_msg}】"
            app.logger.info(msg)
            return jsonify(result_data)
        else:
            if airline_company in OUTLAND_COMPANY:
                if not proxy:
                    msg = f"航司【{airline_company}】占舱转发代理为空"
                    return_error['msg'] = msg
                    app.logger.info(msg)
                    return jsonify(return_error)
            
                try:
                    url = proxy + f"/occupy/{airline_company}/"
                    response = requests.post(url=url, json=get_dict, timeout=180)
                    result_data = response.json()
                    result_msg = result_data.get('msg')
                except Exception as ex:
                    msg = f"航司【{airline_company}】占舱转发代理超时"
                    return_error['msg'] = msg
                    app.logger.info(msg)
                    app.logger.info(ex)
                    return jsonify(return_error)
                else:
                    end_time = (time.time() - start_time).__round__(2)
                    msg = f"航司【{airline_company}】占舱请求返回成功【{end_time}】【{order_no}】【{result_msg}】"
                    app.logger.info(msg)
                    return jsonify(result_data)
            else:
                msg = f"航司【{airline_company}】占舱功能还未上线"
                return_error['msg'] = msg
                app.logger.info(msg)
                return jsonify(return_error)


# # # 链接地址,例http://x.x.x.x:18081/proxy/sl/
@app.route('/proxy/<airline_company>/', methods=['POST'])
def proxy(airline_company: str="") -> dict:
    """代理接口
    :param airline_company:  航司二字码
    :return:  dict
    """
    # # # 检查各项请求参数
    if not request.get_data():
        msg = f"航司【{airline_company}】代理请求数据为空"
        return_error['msg'] = msg
        app.logger.info(msg)
        return jsonify(return_error)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=18081)
