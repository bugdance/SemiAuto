#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    解析器用于解析数据结构, 接入解析器
written by pyleo.
"""


class CallInParser:
    """接入解析器

    """
    
    def __init__(self, corp_enabled: bool=True):
        """
        :param corp_enabled:  是否是企业账户占舱 type(True/False)
        """
        self.logger: any = None                         # 日志记录器
        self.corp_enabled: bool = corp_enabled          # 是否是企业类型
        
        self.occupy_id: any = None                      # 任务编号
        self.account_agent: str = ""                    # 企业账号
        self.account: str = ""                          # 个人账号
        self.username: str = ""                         # 最终用的用户名
        self.password: str = ""                         # 最终用的密码
        self.departure_code: str = ""                   # 始发三字码
        self.arrival_code: str = ""                     # 到达三字码
        self.flight_num: list = []                      # 航班列表
        self.segment_num: int = 0                       # 航段数量
        self.flight_date: str = ""                      # 出发日期
        self.promo: str = ""                            # 优惠码
        self.currency: str = ""                         # 默认货币类型
        self.contact_last: str = ""                     # 联系人姓氏
        self.contact_first: str = ""                    # 联系人名字
        self.contact_email: str = ""                    # 联系邮箱
        self.contact_mobile: str = ""                   # 联系电话
        
        self.adult_list: list = []                      # 成人列表明细
        self.child_list: list = []                      # 儿童列表明细
        self.infant_list: list = []                     # 婴儿列表明细
        self.adult_num: int = 0                         # 成人人数
        self.child_num: int = 0                         # 儿童人数
        self.infant_num: int = 0                        # 婴儿人数

        self.return_baggage: list = []                  # 返回行李列表, 带名字原样返回
        self.return_order: int = 1                      # 返回是否企业占舱标识

    def parse_to_data(self, data_dict: dict=None) -> bool:
        """解析数据
        :param data_dict:  接口传入数据
        :return:  bool
        """
        if not data_dict or type(data_dict) is not dict:
            self.logger.info("解析数据非法传参(*>﹏<*)【{}】".format(data_dict))
            return False
        self.logger.info(f"解析数据以前传参(*>﹏<*)【{data_dict}】")
        
        self.username = data_dict.get('userName')
        self.password = data_dict.get('password')

        self.occupy_id = data_dict.get('orderNO')
        self.departure_code = data_dict.get('depAirCode')
        self.arrival_code = data_dict.get('arrAircode')
        self.flight_date = data_dict.get('depDate')
        self.contact_last = "Wang"
        self.contact_first = "XiaoDao"
        self.contact_email = "hthy666@vip.163.com"
        self.contact_mobile = "16639163387"             # 13810254174
        self.promo = ""
        self.currency = data_dict.get("currency")

        flight_num = data_dict.get('flightNum')
        if not self.parse_to_flights(flight_num):
            return False

        passengers_list = data_dict.get('passengersDataList')
        if not self.parse_to_passengers(passengers_list):
            return False

        return True

    def parse_to_flights(self, flight_num: str="") -> bool:
        """解析航班
        :param flight_num:  接口传入航班
        :return:  bool
        """
        if not flight_num or type(flight_num) is not str or "," in flight_num:
            self.logger.info("解析数据非法航线(*>﹏<*)【{}】".format(flight_num))
            return False

        self.flight_num = flight_num.split('-')
        self.segment_num = len(self.flight_num)
        return True

    def parse_to_passengers(self, passengers_list: list=None) -> bool:
        """解析乘客
        :param passengers_list:  接口传入乘客
        :return:  bool
        """
        if not passengers_list or type(passengers_list) is not list:
            self.logger.info("解析数据非法乘客(*>﹏<*)【{}】".format(passengers_list))
            return False

        for n, v in enumerate(passengers_list):
            full_name = v.get('passengerName')                           # 姓名
            age_type = v.get('ageType')                            # 乘客类型 type(0,成人/1,儿童/2,婴儿)
            gender = v.get('gender')                            # 性别 type(M/F)
            birthday = v.get('birthday')                      # 生日
            nationality = v.get('nationality')                  # 国籍
            card_num = v.get('cardNum')                         # 护照
            card_expired = v.get('cardExpired')                 # 护照时间
            card_place = v.get('cardIssuePlace')                # 护照签发地
            baggage = v.get('baggage')                          # 行李

            if not full_name or not birthday or not gender or type(age_type) is not int:
                self.logger.info("解析数据非法乘客(*>﹏<*)【{}】【{}】".format(n, v))
                return False

            self.return_baggage.append({"passengerName": full_name, "baggage": baggage})

            name_list = full_name.split('/')
            if len(name_list) < 2:
                self.logger.info("解析数据非法姓名(*>﹏<*)【{}】【{}】".format(n, full_name))
                return False

            # # # 组合数据
            list_data = {
                "last_name": name_list[0], "first_name": name_list[1],
                "birthday": birthday,
                "gender": gender, "nationality": nationality, "card_num": card_num,
                "card_expired": card_expired, "card_place": card_place, "baggage": baggage
            }
            if age_type == 0:
                self.adult_list.append(list_data)
            elif age_type == 1:
                self.child_list.append(list_data)
            elif age_type == 2:
                self.infant_list.append(list_data)

        self.adult_num = len(self.adult_list)
        self.child_num = len(self.child_list)
        self.infant_num = len(self.infant_list)

        if not self.adult_num:
            self.logger.info("解析数据非法成人(*>﹏<*)【{}】".format(passengers_list))
            return False
        return True






















    # def parse_to_data(self, data_dict: dict=None) -> bool:
    #     """解析数据
    #     :param data_dict:  接口传入数据
    #     :return:  bool
    #     """
    #     if not data_dict or type(data_dict) is not dict:
    #         self.logger.info("解析数据非法传参(*>﹏<*)【{}】".format(data_dict))
    #         return False
    #
    #     self.account_agent = data_dict.get('carrierAccountAgent')
    #     self.account = data_dict.get('carrierAccount')
    #     if self.corp_enabled:
    #         self.username = self.account_agent
    #         self.password = data_dict.get('carrierPasswordAgent')
    #     else:
    #         self.return_order = 2
    #         self.username = self.account
    #         self.password = data_dict.get('carrierPassword')
    #     if not self.account or not self.password:
    #         self.logger.info("解析数据非法账户(*>﹏<*)【{}】【{}】".format(self.account, self.password))
    #         return False
    #
    #     self.occupy_id = data_dict.get('occupyCabinId')
    #     self.departure_code = data_dict.get('departureAirport')
    #     self.arrival_code = data_dict.get('arriveAirport')
    #     self.flight_date = data_dict.get('departureTime')
    #     self.contact_last = "Li"
    #     self.contact_first = "Jian"
    #     self.contact_email = "168033518@qq.com"
    #     self.contact_mobile = "13717573545"
    #     self.promo = ""
    #     self.currency = data_dict.get("currency")
    #
    #     flight_num = data_dict.get('flightNumber')
    #     if not self.parse_to_flights(flight_num):
    #         return False
    #
    #     passengers_list = data_dict.get('passenger')
    #     if not self.parse_to_passengers(passengers_list):
    #         return False
    #
    #     return True
    #
    # def parse_to_flights(self, flight_num: str="") -> bool:
    #     """解析航班
    #     :param flight_num:  接口传入航班
    #     :return:  bool
    #     """
    #     if not flight_num or type(flight_num) is not str or "," in flight_num:
    #         self.logger.info("解析数据非法航线(*>﹏<*)【{}】".format(flight_num))
    #         return False
    #
    #     self.flight_num = flight_num.split('-')
    #     self.segment_num = len(self.flight_num)
    #     return True
    #
    # def parse_to_passengers(self, passengers_list: list=None) -> bool:
    #     """解析乘客
    #     :param passengers_list:  接口传入乘客
    #     :return:  bool
    #     """
    #     if not passengers_list or type(passengers_list) is not list:
    #         self.logger.info("解析数据非法乘客(*>﹏<*)【{}】".format(passengers_list))
    #         return False
    #
    #     for n, v in enumerate(passengers_list):
    #         full_name = v.get('name')                           # 姓名
    #         age_type = v.get('type')                            # 乘客类型 type(0,成人/1,儿童/2,婴儿)
    #         gender = v.get('gender')                            # 性别 type(M/F)
    #         birthday = v.get('birthday')                      # 生日
    #         nationality = v.get('nationality')                  # 国籍
    #         card_num = v.get('cardNum')                         # 护照
    #         card_expired = v.get('cardExpired')                 # 护照时间
    #         card_place = v.get('cardIssuePlace')                # 护照签发地
    #         baggage = v.get('baggage')                          # 行李
    #
    #         if not full_name or not birthday or not gender or type(age_type) is not int:
    #             self.logger.info("解析数据非法乘客(*>﹏<*)【{}】【{}】".format(n, v))
    #             return False
    #
    #         self.return_baggage.append({"passengerName": full_name, "baggage": baggage})
    #
    #         name_list = full_name.split('/')
    #         if len(name_list) < 2:
    #             self.logger.info("解析数据非法姓名(*>﹏<*)【{}】【{}】".format(n, full_name))
    #             return False
    #
    #         # # # 组合数据
    #         list_data = {
    #             "last_name": name_list[0], "first_name": name_list[1],
    #             "birthday": birthday,
    #             "gender": gender, "nationality": nationality, "card_num": card_num,
    #             "card_expired": card_expired, "card_place": card_place, "baggage": baggage
    #         }
    #         if age_type == 0:
    #             self.adult_list.append(list_data)
    #         elif age_type == 1:
    #             self.child_list.append(list_data)
    #         elif age_type == 2:
    #             self.infant_list.append(list_data)
    #
    #     self.adult_num = len(self.adult_list)
    #     self.child_num = len(self.child_list)
    #     self.infant_num = len(self.infant_list)
    #
    #     if not self.adult_num:
    #         self.logger.info("解析数据非法成人(*>﹏<*)【{}】".format(passengers_list))
    #         return False
    #     return True
