#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    接收器用于接收接口数据并返回响应数据
written by pyleo.
"""
import sys

sys.path.append('..')  # 导入环境当前目录
from flask import Flask, request, jsonify
import logging
import time
import configparser

from explorer.corptr_jumper import CorpTRJumper


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


# # # 链接地址,例http://x.x.x.x:18083/server/tr/
@app.route('/server/<airline_company>/', methods=['POST'])
def server(airline_company: str = "") -> dict:
    """占舱接口
    :param airline_company:  航司二字码
    :return:  dict
    """
    start_time = time.time()  # 开始计时
    return_error = {}
    # # # 检查各项请求参数
    if airline_company == "tr":
        if request.get_data():
            try:
                get_dict = eval(request.get_data())
                order_no = get_dict.get('occupy_id')
            except Exception as ex:
                msg = f"航司【{airline_company}】占舱数据格式有误"
                return_error['msg'] = msg
                app.logger.info(msg)
                app.logger.info(ex)
                return jsonify(return_error)
            else:
                if order_no:
                    log_path = "log/{}-{}.log".format(airline_company, order_no)
                    # # # 生成全局变量数组，声明变量类
                    create_var = globals()
                    scraper = create_var["Corp" + airline_company.upper() + "Jumper"]()
                    result_data = scraper.process_to_main(order_no, log_path, get_dict, False, "")
                    end_time = (time.time() - start_time).__round__(2)
                    msg = f"航司【{airline_company}】占舱请求返回成功【{end_time}】【{order_no}】"
                    app.logger.info(msg)
                    return jsonify(result_data)
                
                else:
                    msg = f"航司【{airline_company}】占舱数据标识为空"
                    return_error['msg'] = msg
                    app.logger.info(msg)
                    return jsonify(return_error)
        else:
            msg = f"航司【{airline_company}】占舱请求数据为空"
            return_error['msg'] = msg
            app.logger.info(msg)
            return jsonify(return_error)
    else:
        msg = f"航司【{airline_company}】占舱功能还未上线"
        return_error['msg'] = msg
        app.logger.info(msg)
        return jsonify(return_error)


# # # 链接地址,例http://x.x.x.x:18083/payment/tr/
@app.route('/payment/<airline_company>/', methods=['POST'])
def payment(airline_company: str = "") -> dict:
    """占舱接口
    :param airline_company:  航司二字码
    :return:  dict
    """
    start_time = time.time()  # 开始计时
    return_error = {}
    # # # 检查各项请求参数
    if airline_company == "tr":
        if request.get_data():
            try:
                get_dict = eval(request.get_data())
                order_no = get_dict.get('occupy_id')
            except Exception as ex:
                msg = f"航司【{airline_company}】占舱数据格式有误"
                return_error['msg'] = msg
                app.logger.info(msg)
                app.logger.info(ex)
                return jsonify(return_error)
            else:
                if order_no:
                    log_path = "log/{}-{}.log".format(airline_company, order_no)
                    # # # 生成全局变量数组，声明变量类
                    create_var = globals()
                    scraper = create_var["Corp" + airline_company.upper() + "Jumper"]()
                    result_data = scraper.process_to_pay(order_no, log_path, get_dict, False, "")
                    end_time = (time.time() - start_time).__round__(2)
                    msg = f"航司【{airline_company}】占舱请求返回成功【{end_time}】【{order_no}】"
                    app.logger.info(msg)
                    return jsonify(result_data)
                
                else:
                    msg = f"航司【{airline_company}】占舱数据标识为空"
                    return_error['msg'] = msg
                    app.logger.info(msg)
                    return jsonify(return_error)
        else:
            msg = f"航司【{airline_company}】占舱请求数据为空"
            return_error['msg'] = msg
            app.logger.info(msg)
            return jsonify(return_error)
    else:
        msg = f"航司【{airline_company}】占舱功能还未上线"
        return_error['msg'] = msg
        app.logger.info(msg)
        return jsonify(return_error)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=18083)
