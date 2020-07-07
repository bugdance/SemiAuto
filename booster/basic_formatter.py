#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    格式器用于格式化数据结构, 基础格式器
written by pyleo.
"""
import copy


class BasicFormatter:
    """基础格式器

    """

    def __init__(self):
        self.logger: any = None  # 日志记录器

    def format_as_same(self, source_data: any = None) -> any:
        """格式镜像
        :param source_data:  来源数据
        :return:  any
        """
        if not source_data:
            self.logger.info(f"格式镜像非法传参(*>﹏<*)【{source_data}】")
        return copy.deepcopy(source_data)

    def format_as_int(self, source_data: any = None) -> int:
        """格式整数
        :param source_data:  来源数据
        :return:  int
        """
        try:
            if type(source_data) is str:
                source_data = source_data.replace(",", "")
            return_data = int(source_data)
        except Exception as ex:
            self.logger.info(f"格式整数返回失败(*>﹏<*)【{source_data}】")
            self.logger.info(f"格式整数失败原因(*>﹏<*)【{ex}】")
            return 0
        else:
            return return_data

    def format_as_float(self, decimal_num: int = 2, source_data: any = None) -> float:
        """格式浮点
        :param decimal_num:  小数点位数
        :param source_data:  来源数据
        :return:  float
        """
        try:
            if type(source_data) is str:
                source_data = source_data.replace(",", "")
            return_data = float(source_data).__round__(decimal_num)
        except Exception as ex:
            self.logger.info(f"格式浮点返回失败(*>﹏<*)【{source_data}】")
            self.logger.info(f"格式浮点失败原因(*>﹏<*)【{ex}】")
            return 0.0
        else:
            return return_data

    def format_as_cut(self, decimal_num: int = 2, source_data: any = None) -> str:
        """截取浮点字符串
        :param decimal_num:  小数点位数
        :param source_data:  来源数据
        :return:  str
        """
        try:
            if type(source_data) is str:
                source_data = source_data.replace(",", "")
            source_data = float(source_data)
            return_data = f"{source_data:.{decimal_num}f}"
        except Exception as ex:
            self.logger.info(f"截取浮点返回失败(*>﹏<*)【{source_data}】")
            self.logger.info(f"截取浮点失败原因(*>﹏<*)【{ex}】")
            return ""
        else:
            return return_data
