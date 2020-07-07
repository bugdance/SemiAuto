#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    采集器用于正式请求网站采集数据, 5J采集器
written by pyleo.
"""
from accessor.request_worker import RequestWorker
from accessor.request_builder import RequestBuilder
from accessor.request_crawler import RequestCrawler
from booster.basic_formatter import BasicFormatter
from booster.basic_parser import BasicParser
from booster.callback_formatter import CallBackFormatter
from booster.callin_parser import CallInParser
from booster.date_formatter import DateFormatter
from booster.dom_parser import DomParser


class PersWNScraper(RequestWorker):
    """WN采集器

    """
    
    def __init__(self) -> None:
        RequestWorker.__init__(self)
        self.RBR = RequestBuilder()  # 请求建造器
        self.RCR = RequestCrawler()  # 请求爬行器
        self.BFR = BasicFormatter()  # 基础格式器
        self.BPR = BasicParser()  # 基础解析器
        self.CFR = CallBackFormatter()  # 回调格式器
        self.CPR = CallInParser(False)  # 接入解析器
        self.DFR = DateFormatter()  # 日期格式器
        self.DPR = DomParser()  # 文档解析器
        
        self.booking_key: str = ""
        self.fare_key: str = ""
        self.passenger_sell: str = ""
        self.hold_button: str = ""
        self.temp_source: str = ""
        # # # 返回中用到的变量
        self.total_price: float = 0.0  # 总价
        self.baggage_price: float = -1  # 行李总价
        self.record: str = ""  # 票号
        self.pnr_timeout: str = ""  # 票号超时时间
    
    def init_to_config(self) -> None:
        """初始化配置
        :return:  None
        """
        # # # 设置日志
        self.RBR.logger = self.logger
        self.RCR.logger = self.logger
        self.BFR.logger = self.logger
        self.BPR.logger = self.logger
        self.CFR.logger = self.logger
        self.CPR.logger = self.logger
        self.DFR.logger = self.logger
        self.DPR.logger = self.logger
        # # # 设置配置和代理
        self.RCR.set_to_configs()
        self.init_header = self.RBR.build_as_header("none")
        self.callback_data = self.CFR.format_as_async()
    
    def process_to_main(self, occupy_id: any = None, log_path: str = "", data_dict: dict = None,
                        enable_proxy: bool = False, address: str = "") -> dict:
        """主体流程，进口和出口
        :param occupy_id:  日志唯一标识
        :param log_path:  日志保存地址
        :param data_dict:  接口传入的字典
        :param enable_proxy:  是否使用代理
        :param address:  代理地址 type(http://1.1.1.1:22443 or http://yunku:123@1.1.1.1:3138)
        :return:  dict
        """
        # # # 初始化日志
        self.init_to_logging(occupy_id, log_path)
        self.init_to_config()
        self.RCR.set_to_proxy(enable_proxy, address)
        # # # 解析接口参数
        if not self.CPR.parse_to_data(data_dict):
            self.callback_data['msg'] = "解析接口数据失败"
            return self.callback_data

        if self.query_from_home():
            if self.query_from_detail():
    #             if self.query_from_passenger():
    #                 if self.query_from_service():
    #                     if self.query_from_payment():
    #                         if self.get_for_record():
                                if self.return_to_data():
                                    self.logout_to_user()
                                    self.logger.removeHandler(self.handler)
                                    return self.callback_data
        
        self.callback_data["occupyCabinId"] = self.CPR.occupy_id
        self.callback_data['msg'] = self.callback_msg
        # self.callback_data['msg'] = "解决认证问题中，请先手工占位，辛苦各位"
        self.callback_data["carrierAccount"] = self.CPR.username
        self.callback_data['carrierAccountAgent'] = ""
        self.logger.info(self.callback_data)
        self.logger.removeHandler(self.handler)
        return self.callback_data
    
    def set_to_proxy(self, count: int = 0, max_count: int = 3) -> bool:
        """切换代理
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        if count >= max_count:
            return False
        else:
            # 获取代理， 并配置代理
            self.RCR.url = 'http://cloudmonitorproxy.51kongtie.com/Proxy/getProxyByServiceType?proxyNum=1&serviceType=4'
            self.RCR.header = self.BFR.format_as_same(self.init_header)
            self.RCR.param_data = None
            if self.RCR.request_to_get('json'):
                for ip in self.RCR.page_source:
                    if ip.get('proxyIP'):
                        proxy = "http://yunku:123@" + str(ip.get('proxyIP')) + ":" + str(ip.get('prot'))
                        self.RCR.set_to_proxy(enable_proxy=True, address=proxy)
                        return True
                    else:
                        self.logger.info("请求代理有问题")
            else:
                self.logger.info("请求代理有问题")
            
            self.logger.info(f"代理第{count + 1}次超时或者错误(*>﹏<*)【proxy】")
            self.callback_msg = f"代理第{count + 1}次超时或者错误"
            return self.set_to_proxy(count + 1, max_count)
    
    def query_from_home(self, count: int = 0, max_count: int = 3) -> bool:
        """首页查询航班流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        if count >= max_count:
            return False
        else:
            # # # 爬取首页
            self.RCR.url = 'https://www.southwest.com/'
            self.RCR.param_data = None
            self.RCR.header = self.BFR.format_as_same(self.init_header)
            self.RCR.header.update({
                "Host": "www.southwest.com",
                "Upgrade-Insecure-Requests": "1",
            })
            self.RCR.post_data = None
            if self.RCR.request_to_get():

                # # # 解析查询页获取token
                self.RCR.url = "https://www.southwest.com/air/booking/select.html"
                query = (
                    ("int", "HOMEQBOMAIR"), ("adultPassengersCount", self.CPR.adult_num + self.CPR.child_num),
                    ("departureDate", self.CPR.flight_date), ("destinationAirportCode", self.CPR.arrival_code), ("fareType", "USD"),
                    ("originationAirportCode", self.CPR.departure_code), ("passengerType", "ADULT"),
                    ("returnDate", ""), ("seniorPassengersCount", "0"),
                    ("tripType", "oneway"), ("departureTimeOfDay", "ALL_DAY"), ("reset", "true"),
                    ("returnTimeOfDay", "ALL_DAY"),
                )
                query_url = self.BPR.parse_as_url(query)
                
                self.RCR.param_data = query
                self.RCR.header = self.BFR.format_as_same(self.init_header)
                self.RCR.header.update({
                    "Host": "www.southwest.com",
                    "Referer": "https://www.southwest.com/",
                    "Upgrade-Insecure-Requests": "1",
                })
                self.RCR.post_data = None
                if self.RCR.request_to_get():
                    
                    self.RCR.url = 'https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/shopping'
                    self.RCR.param_data = None
                    self.RCR.header = self.BFR.format_as_same(self.init_header)
                    self.RCR.header.update({
                        "Accept": "application/json, text/javascript, */*; q=0.01",
                        "Content-Type": "application/json",
                        "Host": "www.southwest.com",
                        "Origin": "https://www.southwest.com",
                        "Referer": "https://www.southwest.com/air/booking/select.html?" + query_url,
                        "X-User-Experience-ID": "07a13dfe-d186-4124-9949-4a97d78fb9d6",
                        "EE30zvQLWf-z": "p",
                        "Authorization": "null null",
                        "EE30zvQLWf-b": "-s9ebqy",
                        "X-Api-IDToken": "null",
                        "EE30zvQLWf-d": "o_0",
                        "EE30zvQLWf-c": "Az99PmNuAQAA7rf6QGGSPR3bURvxvYu0WEzlkEJ7Z8AtiSKdA-UlWv32-jJjAXGsmQGuchAEwH8AAEB3AAAAAA==",
                        "EE30zvQLWf-f": "A4gKQmNuAQAArFECOkdA4yg3uZnMWpZl_E1kqVY8ZqKeaEXD__2AqO30VCYQAXlFMIOucn01wH8AAEB3AAAAAA==",
                        "X-Channel-ID": "southwest",
                        "EE30zvQLWf-a": "HkBdmXuFx9v4NQBP-YMXTlxDMVgKMgoeYhkzkbU-QeEzmsLgjHJPUcqFVGn=eZ=BNnzLEINXkYrVdAw9anRQIq2=joaWl7Nnd1VbQ1BqelimmkHGMpylhyLmkrNetEevElbBE7V__HnJqJ9IzTlz9kjTYHqyOn9qdFERdIpJkxb5w5D=mUBbwTJj3FYyyM5OXFDHOp0C702eex45d4LB6PDoZTshCmT5Qs_EGycD5xOyFeO-_f2jC9-0ZfvYsrPvgEfo4CvyIobahcoNXE1UcZVbNvith2bzQNwV4fnZNuMhYf8N2_nJnPR8jt3hLR3RgK3KinifMP4zJ8BUyIjk4ujpNV5YuL7KP2ye38V5jHt0XKwwUc4RNZ1Oy9cMQwNFF0W6LF3njqzQTA8FwBRO=gP72XKu1r0hWTYBVp4BdVReWeocHL_FJY3xyBhZhcowiglyfHNkCmwR8l0pkAg6QQt1lGCNamaJU3YqcRgMWkMgdu3aGb5xrV0cFu91gmv9JhcecEPQh4sZBjQRNVK7dmbNRUDti3nRrEVD7UMXdf9O7b4e5O72l8atV2t0AE71=lBbAG2KNtxaZ9Xc6jVKdlI0k_MOv2JtLnLRUr=eesaI2ywcoxZ3o3benItb4etr=loO=U5D6X-hZkis0Co=OwGYlOvka6wEb-ldyf96BWEhFwb1XsCKPqt45AFUb05Vp3dJ_9fKy3ZWtONNMr4Ck7p_annAkf8aNr3T4mJxszGVnaBiMP6T2FBBcR=087EM98F8APlWKuTMX7c7wjdW76sJoxme15empfoFI-qWbndXIHYFB_KhATutamgxjjeR4j-x=o=eWP57wc48yyYsNCQc4zqb=3XOvC5qBM54kaXd67Z6aK1-mwudXmw_5JMp1Z91jsqb=6d--z3Kt_c4O01qFKwB_G0IbbGP22wR14skwg-AIs=BavrRyV3=jTkoo9=uN8Zu325jm9mIrJ-DNP9K-pcVrzsWHuTX7nBNzuCcIsZkoVGeIiH_pb4Ao93Me9g7bROhLYqtxIEywGo9rpqIHpd=ZHDQpe-AjTaQDsWlwlRu3lTJa738jFLax-e9=kE9gopMJwECpKsAB=0ZDhfDy6U5qhUNqKDcvowt79-eReM=e2KjdWhmyLWHACrtGz9DUqOV4ihmf61iYOXgzrPWNxCD9Jj53qbuXHs_NMyIi7cdXPQ0sb=C1Q8=kreJlCHEBFthGfbd=mUjZp6vcrYVcCTFNdAUWs=0996TqFr-r1zUfWu9d=HGXgwxCs15PdisWrdB6WsfrqZi3BchoM3VtWJe8EhGJTFsAR6CtYrecw4reM67O0WvRudco7n2_d6-4p9Tsxs0_VY8gfHPwDFmq_Zum969ng=2nXL-5usMpqtlalVO5Y1JgjjB4h0DTkRHVYm=jlsHfFiPiaO33DXLq3b8RAq_I1EiPFeN-oKmbLqrG7rv0=hx0Lifr59II24cFNUp8KWzm9wIZC01gLoOUMeDkL_6eRZkszZE7IfNrl5EUm3tFCjZTNsqk0EMUAWKHNKjzJUrFa=H569fg3XOniIECs1Zjg3=ncs35LYnq67swR-FdOmVwIDFtOlldk-a",
                        "X-API-Key": "l7xx944d175ea25f4b9c903a583ea82a1c4c"
                    })
                    self.RCR.post_data = {"int": "HOMEQBOMAIR", "adultPassengersCount": self.CPR.adult_num + self.CPR.child_num,
                                          "departureDate": self.CPR.flight_date, "destinationAirportCode": self.CPR.arrival_code,
                                          "fareType": "USD", "originationAirportCode": self.CPR.departure_code,
                                          "passengerType": "ADULT", "returnDate": "", "seniorPassengersCount": "0",
                                          "tripType": "oneway", "departureTimeOfDay": "ALL_DAY", "reset": "true",
                                          "returnTimeOfDay": "ALL_DAY", "application": "air-booking", "site": "southwest"}
                    if self.RCR.request_to_post("json", "json"):
                        return True
            
            self.logger.info(f"查询第{count + 1}次超时或者错误(*>﹏<*)【home】")
            self.callback_msg = f"查询第{count + 1}次超时或者错误"
            return self.query_from_home(count + 1, max_count)
    
    def query_from_detail(self, count: int = 0, max_count: int = 3):
        
        details, temp_list = self.BPR.parse_as_path("$.data.searchResults.airProducts[0].details", self.RCR.page_source)
        if not details and type(details) is not list:
            self.logger.info(f"获取不到航线数据(*>﹏<*)【{self.CPR.departure_code}】【{self.CPR.arrival_code}】")
            return False
        
        is_flight = 0
        flightNumbers = ""
        stopsDetails = []
        departureTime = ""
        arrivalTime = ""
        product_id = ""
        select_type = ""
        fareData = {}
        upgrade_type = ""
        upgradeFare = {}
        sum_dict = {}
    
        for i in details:
            stopsDetails = i.get('stopsDetails')
            if not stopsDetails or len(stopsDetails) != self.CPR.segment_num:
                continue
        
            flights = []
            for j in self.CPR.flight_num:
                flight_no = j[2:]
                flight_no = self.BFR.format_as_int(flight_no)
                if flight_no:
                    flights.append(flight_no)
                    
            flight_num = []
            for j in i.get('flightNumbers'):
                flight_no = self.BFR.format_as_int(j)
                if flight_no:
                    flight_num.append(flight_no)
        
            if flight_num == flights:
                self.logger.info(f"匹配航班信息成功(*^__^*)【{self.CPR.flight_num}】")
                is_flight = 1
                flightNumbers = i.get('flightNumbers')
                stopsDetails = i.get('stopsDetails')
                departureTime = i.get('departureTime')
                arrivalTime = i.get('arrivalTime')

                adult, temp_list = self.BPR.parse_as_path("$.fareProducts.ADULT", i)
                if not adult:
                    self.logger.info(f"获取不到航班数据(*>﹏<*)【{self.CPR.flight_num}】")
                    return False
                
                price_dict = {}
                for k, v in adult.items():
                    price, temp_list = self.BPR.parse_as_path("$.fare.totalFare.value", v)
                    status, temp_list = self.BPR.parse_as_path("$.availabilityStatus", v)
                    if price:
                        sum_dict[k] = price
                        price_dict[k] = price
                    else:
                        sum_dict[k] = status
                    
                if not price_dict:
                    self.logger.info(f"该航班座位已售完(*>﹏<*)【{self.CPR.flight_num}】")
                    self.callback_msg = "该航班座位已售完"
                    return False
                price_list = sorted(price_dict.values())
                select_price = price_list[0]
                upgrade_price = price_list[-1]
                for k, v in price_dict.items():
                    if v == select_price:
                        select_type = k
                    elif v == upgrade_price:
                        upgrade_type = k
                        
                product_id = i['fareProducts']['ADULT'][select_type]['productId']
                fareData = i['fareProducts']['ADULT'][select_type]
                upgradeFare = i['fareProducts']['ADULT'][upgrade_type]
                print(product_id)
                break
    
        if not is_flight:
            self.logger.info(f"匹配不到航班信息(*>﹏<*)【{self.CPR.flight_num}】")
            self.callback_msg = f"匹配不到航班信息【{self.CPR.flight_num}】"
            return False
        else:

            self.RCR.url = 'https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/price'
            self.RCR.param_data = None
            self.RCR.post_data = {
                "adultPassengersCount": "1", "currencyCode": "USD", "currencyType": "REVENUE",
                "requiredPricingInfo": True, "segmentProducts": [{"ADULT": product_id}],
                "seniorPassengersCount": "0", "application": "air-booking", "site": "southwest"}
            if self.RCR.request_to_post("json", "json"):
                itineraryPricings, temp_list = self.BPR.parse_as_path("$.data.priceFlightsResults.itineraryPricings", self.RCR.page_source)
                now = self.DFR.format_from_now()
                self.RCR.url = 'https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/purchase'
                self.RCR.param_data = None
                self.RCR.header.update({
                    "Referer": "https://www.southwest.com/air/booking/price.html"
                })
                self.RCR.post_data = {
                    "air": {
                        "fares": {
                            "0": {
                                "departureDate": self.CPR.flight_date,
                                "destinationAirportCode": self.CPR.arrival_code,
                                "international": False,
                                "nextDay": False,
                                "originationAirportCode": self.CPR.departure_code,
                                "stopsDetails": stopsDetails,
                                "ADULT": {
                                    "arrivalTime": arrivalTime,
                                    "departureTime": departureTime,
                                    "fareData": fareData,
                                    "fareType": select_type,
                                    "flightNumbers": flightNumbers,
                                    "hasUpgradeData": False,
                                    "nextDay": False,
                                    "rowSummary": sum_dict,
                                    "stopsDetails": stopsDetails,
                                    "upgradeFare": upgradeFare,
                                    "drawerUpgradeAccepted": False,
                                    "drawerUpgradeOffered": False,
                                    "modalUpgradeAccepted": False,
                                    "modalUpgradeOffered": False
                                }
                            }
                        },
                        "id": "air",
                        "query": {
                            "int": "HOMEQBOMAIR", "adultPassengersCount": self.CPR.adult_num + self.CPR.child_num,
                            "departureDate": self.CPR.flight_date, "destinationAirportCode": self.CPR.arrival_code,
                            "fareType": "USD", "originationAirportCode": self.CPR.departure_code,
                            "passengerType": "ADULT", "returnDate": "", "seniorPassengersCount": "0",
                            "tripType": "oneway", "departureTimeOfDay": "ALL_DAY", "reset": "true",
                            "returnTimeOfDay": "ALL_DAY"
                        },
                        "earlyBirdProduct": None,
                        "funds": None,
                        "unaccompaniedMinorFee": None,
                        "itineraryPricings": itineraryPricings,
                        "lastPriceUpdate": now.strftime("%Y-%m-%dT%H:%M:%S+08:00")
                    },
                    "ancillaryType": ["EARLY_BIRD", "UNACCOMPANIED_MINOR"],
                    "chaseApplied": False,
                    "application": "air-booking",
                    "site": "southwest"
                }
                if self.RCR.request_to_post("json", "json"):
                    print(self.RCR.page_source)
                    print(self.RCR.get_from_cookies())
                    return True

        self.logger.info(f"查询第{count + 1}次超时或者错误(*>﹏<*)【home】")
        self.callback_msg = f"查询第{count + 1}次超时或者错误"
        return self.query_from_detail(count + 1, max_count)
    
    def query_from_passenger(self, count: int = 0, max_count: int = 3) -> bool:
        """查询乘客信息流程
        :param count:  重试次数
        :param max_count:  重试最大次数
        :return:  bool
        """
        if count >= max_count:
            return False
        else:
            # # # 解析详情页
            self.RCR.url = "https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/confirmation"
            self.RCR.param_data = None
            self.RCR.header = self.BFR.format_as_same(self.init_header)
            self.RCR.header.update({
                "Referer": "https://www.southwest.com/air/booking/purchase.html"
            })
            self.RCR.post_data = {
                "planSectionFirstEmail": "",
                "planSectionSecondEmail": "",
                "planSectionThirdEmail": "",
                "planSectionFourthEmail": "",
                "fundsCoverTotalFlight": False,
                "paymentMethodSelected": "creditcard",
                "savedCreditCardSelected": False,
                "cvvHidden": False,
                "aboutTripBusinessCheckBox": False,
                "aboutTripFirstTimeCheckBox": False,
                "aboutTripPersonalCheckBox": True,
                "savedEmailAddress": "",
                "savedReceiptEmailSelected": False,
                "sendYourReceiptEmail": "168033518@qq.com",
                "contactCountryCode": "1",
                "contactEmailAddress": "168033518@qq.com",
                "contactMethod": "email",
                "contactOptOut": False,
                "contactPhoneNumber": "",
                "contactPreferredLanguage": "EN",
                "cartProducts": {},
                "chaseSessionId": None,
                "minorFormData": None,
                "pointsToUse": 0,
                "selectedCardInfo": None,
                "application": "air-booking",
                "site": "southwest",
                "creditCard": {
                    "cardNumber": "5329591870277432",
                    "cityTown": "BEIJING",
                    "country": "CN",
                    "countryCode": "86",
                    "creditCardType": "MASTERCARD",
                    "expiration": "11-2021",
                    "firstNameOnCard": "JIAN",
                    "lastNameOnCard": "WANG",
                    "phoneNumber": "18630806256",
                    "primary": False,
                    "provinceRegion": "BEIJING",
                    "securityCode": "371",
                    "state": "",
                    "streetAddress": "BEIJING",
                    "streetAddressSecond": "",
                    "zipCode": "100000",
                    "zipCodeRequired": True
                },
                "dutyOfCareContactInfo": {},
                "passengersList": [{
                    "passengerFirstName": "KUN",
                    "passengerMiddleName": "",
                    "passengerLastName": "FENG",
                    "passengerSuffix": "0",
                    "passengerGender": "FEMALE",
                    "passengerDateOfBirth": "1995-09-22",
                    "passengerRapidRewards": "",
                    "passengerRedressTravelerNumber": "",
                    "passengerKnownTravelerNumber": "",
                    "passengerPassportCountryOfResidence": "",
                    "passengerPassportExpirationDate": "",
                    "passengerPassportIssuedBy": "",
                    "passengerPassportNationality": "",
                    "passengerPassportNumber": "",
                    "passengerDisabilityBlind": False,
                    "passengerDisabilityDeaf": False,
                    "passengerDisabilityCognitive": False,
                    "passengerDisabilityAssistanceAnimal": False,
                    "passengerDisabilityEmotionalAnimal": False,
                    "passengerDisabilityWheelchairAssistance": "NO_NEEDED",
                    "passengerDisabilityWheelchairStowage": "NO_NEEDED",
                    "passengerDisabilitySpillableBatteries": "0",
                    "passengerDisabilityNonSpillableBatteries": "0",
                    "passengerDisabilityPeanut": False,
                    "passengerDisabilityOxygen": False,
                    "passengerType": "ADULT"
                }]
            }
            if self.RCR.request_to_post("json", "json"):
                print(self.RCR.page_source)
                print(self.RCR.get_from_cookies())
                return True
            
            self.logger.info(f"乘客第{count + 1}次超时或者错误(*>﹏<*)【passenger】")
            self.callback_msg = f"乘客第{count + 1}次超时或者错误"
            return self.query_from_passenger(count + 1, max_count)
    
    def return_to_data(self) -> bool:
        """返回结果数据
        :return:  bool
        """
        self.callback_data["success"] = "true"
        self.callback_data['msg'] = "占舱成功"
        self.callback_data["occupyCabinId"] = self.CPR.occupy_id
        self.callback_data['totalPrice'] = self.total_price
        self.callback_data["currency"] = self.CPR.currency
        self.callback_data['pnrCode'] = self.record
        self.callback_data["pnrTimeout"] = self.pnr_timeout
        self.callback_data['orderSrc'] = self.CPR.return_order
        self.callback_data["carrierAccount"] = self.CPR.username
        self.callback_data['carrierAccountAgent'] = ""
        self.callback_data["baggagePrice"] = self.baggage_price
        self.callback_data['passengerBaggages'] = self.CPR.return_baggage
        self.logger.info(self.callback_data)
        return True

