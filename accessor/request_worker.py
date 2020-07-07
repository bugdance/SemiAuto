#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Tue Jul 09 05:58:50 UTC+8:00 2019
    工作器用于制作工作流，request工作器
written by pyleo.
"""
import logging


class RequestWorker:
    """request工作器

    """

    def __init__(self):
        self.logger: any = None  # 日志记录器
        self.handler: any = None  # 日志处理器
        self.init_header: dict = {}  # 初始化请求头
        self.callback_data: dict = {}  # 回调数据
        self.callback_msg: str = "占舱失败"  # 回调信息

    def init_to_logging(self, occupy_id: any = None, log_path: str = ""):
        """初始化日志
        :param occupy_id:  日志唯一标识
        :param log_path:  日志保存地址
        :return:
        """
        self.logger = logging.getLogger(str(occupy_id))
        self.logger.setLevel(level=logging.INFO)
        formatter = logging.Formatter("[%(asctime)s]%(message)s")
        # self.handler = logging.FileHandler(log_path, encoding="utf-8")
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def init_to_config(self):
        """初始化配置
        :return:
        """
        pass

    def process_to_main(self, quality_id: any = None, log_path: str = "", data_dict: dict = None,
                        enable_proxy: bool = False, address: str = "") -> dict:
        """主体流程，进口和出口
        :param quality_id:  日志唯一标识
        :param log_path:  日志保存地址
        :param data_dict:  接口传入的字典
        :param enable_proxy:  是否使用代理
        :param address:  代理地址 type(http://1.1.1.1:22443 or http://yunku:123@1.1.1.1:3138)
        :return:  dict
        """
        pass

    def pass_to_verify(self, count: int = 0, max_count: int = 3) -> bool:
        """认证流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass

    def login_to_user(self, count: int = 0, max_count: int = 3) -> bool:
        """登录流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass

    def logout_to_user(self) -> bool:
        """退出流程
        :return:  bool
        """
        pass

    def query_from_login(self, count: int = 0, max_count: int = 3) -> bool:
        """登录后查询航班流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass

    def query_from_home(self, count: int = 0, max_count: int = 3) -> bool:
        """首页查询航班流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass

    def query_from_detail(self, count: int = 0, max_count: int = 3) -> bool:
        """查询航班详情信息流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass

    def matching_to_flight(self) -> bool:
        """匹配航班信息流程
        :return:  bool
        """
        pass

    def query_from_passenger(self, count: int = 0, max_count: int = 3) -> bool:
        """查询乘客信息流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass

    def query_from_service(self, count: int = 0, max_count: int = 3) -> bool:
        """查询附加服务信息流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass
    
    def query_from_payment(self, count: int = 0, max_count: int = 3) -> bool:
        """查询支付信息流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass

    def get_for_record(self, count: int = 0, max_count: int = 3) -> bool:
        """获取订单号流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        pass

    def collect_to_segments(self) -> bool:
        """收集航段信息
        :return:  bool
        """
        pass

    def collect_to_passengers(self) -> bool:
        """收集乘客信息
        :return:  bool
        """
        pass

    def compare_to_data(self) -> bool:
        """对比首页结果和登录结果
        :return:  bool
        """
        pass

    def return_to_data(self) -> bool:
        """返回结果数据
        :return:  bool
        """
        pass

