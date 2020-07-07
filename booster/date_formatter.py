#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    格式器用于格式化数据结构, 日期格式器
written by pyleo.
"""
from datetime import datetime, timedelta
import pytz
import re


class DateFormatter:
    """日期格式器

    """

    def __init__(self):
        self.logger: any = None  # 日志记录器

    def format_from_transform(self, source_time: str = "", source_format: str = "") -> datetime:
        """格式时间转换
        :param source_time:  来源日期数据
        :param source_format:  来源日期的格式
        :return:  datetime
        """
        try:
            return_date = datetime.strptime(source_time, source_format)
        except Exception as ex:
            self.logger.info(f"格式时间转换失败(*>﹏<*)【{source_time}】")
            self.logger.info(f"格式时间失败原因(*>﹏<*)【{ex}】")
            return datetime.now()
        else:
            return return_date

    def format_from_now(self, custom_days: float = 0, custom_hours: float = 0,
                        custom_minutes: float = 0, custom_seconds: float = 0) -> datetime:
        """格式现在时间差
        :param custom_days:  计算天数差
        :param custom_hours:  计算小时差
        :param custom_minutes:  计算分钟差
        :param custom_seconds:  计算秒差
        :return:  datetime
        """
        try:
            return_date = datetime.now() + timedelta(
                days=custom_days, hours=custom_hours, minutes=custom_minutes, seconds=custom_seconds)
        except Exception as ex:
            self.logger.info(f"格式现在时差失败(*>﹏<*)【now】")
            self.logger.info(f"格式现在失败原因(*>﹏<*)【{ex}】")
            return datetime.now()
        else:
            return return_date

    def format_from_custom(self, source_time: str = "", source_format: str = "",
                           custom_days: float = 0, custom_hours: float = 0,
                           custom_minutes: float = 0, custom_seconds: float = 0) -> datetime:
        """格式指定时间差
        :param source_time:  来源日期数据
        :param source_format:  来源日期的格式
        :param custom_days:  计算天数差
        :param custom_hours:  计算小时差
        :param custom_minutes:  计算分钟差
        :param custom_seconds:  计算秒差
        :return:  datetime
        """
        try:
            custom_date = datetime.strptime(source_time, source_format)
            return_date = custom_date + timedelta(
                days=custom_days, hours=custom_hours, minutes=custom_minutes, seconds=custom_seconds)
        except Exception as ex:
            self.logger.info(f"格式指定时间失败(*>﹏<*)【{source_time}】")
            self.logger.info(f"格式指定失败原因(*>﹏<*)【{ex}】")
            return datetime.now()
        else:
            return return_date

    def format_from_timestamp(self, time_stamp: str = "", divided: int = 1000) -> datetime:
        """格式时间戳
        :param time_stamp:  来源时间戳
        :param divided:  来源时间除以的比率
        :return:  datetime
        """
        try:
            date_string = re.findall("-?\d+", time_stamp, re.S)
            date_seconds = int(date_string[0]) / divided
            return_date = datetime(1970, 1, 1) + timedelta(seconds=date_seconds)
        except Exception as ex:
            self.logger.info(f"格式时戳时间失败(*>﹏<*)【{time_stamp}】")
            self.logger.info(f"格式时戳失败原因(*>﹏<*)【{ex}】")
            return datetime.now()
        else:
            return return_date

    def format_from_timezone(self, time_stamp: str = "", time_zone: str = "", divided: int = 1000) -> datetime:
        """格式时区
        :param time_stamp:  来源时间戳
        :param time_zone:  时区
        :param divided:  来源时间除以的比率
        :return:  datetime
        """
        try:
            date_string = re.findall("-?\d+", time_stamp, re.S)
            date_seconds = int(date_string[0]) / divided
            tz = pytz.timezone(time_zone)
            return_date = datetime.fromtimestamp(date_seconds, tz)
        except Exception as ex:
            self.logger.info(f"格式时区时间失败(*>﹏<*)【{time_stamp}】")
            self.logger.info(f"格式时区失败原因(*>﹏<*)【{ex}】")
            return datetime.now()
        else:
            return return_date

    def format_from_utc(self, source_time: str = "") -> datetime:
        """格式格林时间
        :param source_time:  来源数据  2019-09-30T14:00:00+08:00
        :return:  datetime
        """
        try:
            base_time = source_time[:-6]
            add_time = source_time[-6:]
            base_time = datetime.strptime(base_time, "%Y-%m-%dT%H:%M:%S")
            custom_hours = int(add_time[1:3])
            custom_minutes = int(add_time[4:])
            if "+" in add_time:
                return_date = base_time + timedelta(hours=custom_hours, minutes=custom_minutes)
            else:
                return_date = base_time - timedelta(hours=custom_hours, minutes=custom_minutes)
        except Exception as ex:
            self.logger.info(f"格式格林时间失败(*>﹏<*)【{source_time}】")
            self.logger.info(f"格式格林失败原因(*>﹏<*)【{ex}】")
            return datetime.now()
        else:
            return return_date
