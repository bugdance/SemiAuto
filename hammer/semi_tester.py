#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019

written by pyleo.
"""
import sys
sys.path.append('..')                           # 导入环境当前目录

# # # 模拟接口
import requests
from explorer.perswn_scraper import PersWNScraper





# occupyCabinId = 5548
# departureAirport = "DMK"
# arriveAirport = "KUL"
# departureTime = "20190910"
# flightNumber = "OD0521"
# carrierAccount = "QCYG014"
# carrierPassword = "Hthy@1234"
# carrierAccountAgent = "QCYG014"
# carrierPasswordAgent = "Hthy@1234"

occupyCabinId = 5548
departureAirport = "SLC"
arriveAirport = "LAX"
departureTime = "2019-11-30"
flightNumber = "WN2840-WN4800"
carrierAccount = "QCYG014"
carrierPassword = "Hthy@1234"
carrierAccountAgent = "QCYG014"
carrierPasswordAgent = "Asdfg@4321"


# post_data = {
#     "occupyCabinId": occupyCabinId,
#     "carrierCode": "VJ",
#     "departureAirport": departureAirport,
#     "arriveAirport": arriveAirport,
#     "flightNumber": flightNumber,
#     "departureTime": departureTime,
#     "carrierAccount": carrierAccount,
#     "carrierPassword": carrierPassword,
#     "carrierAccountAgent": carrierAccountAgent,
#     "carrierPasswordAgent": carrierPasswordAgent,
#     "currency": "",
#     "passenger": [
#         {"name": "xiang/shaolong",
#          "type": 0,
#          "gender": "M",
#          "birthday": "19840526",
#          "nationality": "CN",
#          "cardNum": "E18269332",
#          "cardExpired": "20240526",
#          "cardIssuePlace": "CN",
#          "cardType": "PP",
#          "baggage": [
#              {"number": 1, "weight": 20}
#          ],
#          },
#
#
#     ],
#     "crawlerType": "2",
# }

post_data = {
    "orderNO": occupyCabinId,
    "carrierCode": "VJ",
    "depAirCode": departureAirport,
    "arrAircode": arriveAirport,
    "flightNum": flightNumber,
    "depDate": departureTime,
    "carrierAccount": carrierAccount,
    "carrierPassword": carrierPassword,
    "userName": carrierAccount,
    "password": carrierPassword,
    "currency": "",
    "passengersDataList": [
        {"passengerName": "zhou/bapi",
         "ageType": 0,
         "gender": "M",
         "birthday": "1973-01-26",
         "nationality": "CN",
         "cardNum": "E18269133",
         "cardExpired": "20240526",
         "cardIssuePlace": "CN",
         "cardType": "PP",
         "baggage": [
             # {"number": 1, "weight": 5}
         ],
         },
        {"passengerName": "zhou/babo",
         "ageType": 0,
         "gender": "F",
         "birthday": "1975-05-26",
         "nationality": "CN",
         "cardNum": "E18269332",
         "cardExpired": "20240526",
         "cardIssuePlace": "CN",
         "cardType": "PP",
         "baggage": [
             # {"number": 1, "weight": 20}
         ],
         },
        # {"passengerName": "xxx/shaolong",
        #  "ageType": 1,
        #  "gender": "F",
        #  "birthday": "2012-05-26",
        #  "nationality": "CN",
        #  "cardNum": "E18269332",
        #  "cardExpired": "20240526",
        #  "cardIssuePlace": "CN",
        #  "cardType": "PP",
        #  "baggage": [
        #      # {"number": 1, "weight": 20}
        #  ],
        #  },
        # {"passengerName": "yyy/shaong",
        #  "ageType": 1,
        #  "gender": "M",
        #  "birthday": "2011-05-26",
        #  "nationality": "CN",
        #  "cardNum": "E18269332",
        #  "cardExpired": "20240526",
        #  "cardIssuePlace": "CN",
        #  "cardType": "PP",
        #  "baggage": [
        #      {"number": 1, "weight": 20}
        #  ],
        #  },

    ],
    "crawlerType": "2",
}




def post_test():
    """
    :return:
    """
    company = "xw"
    url = "http://119.3.249.135:18081/occupy/{}/".format(company)
    response = requests.post(url=url, json=post_data)
    print(response.text)


if __name__ == '__main__':
    # post_test()
    # import time
    # while 1:
    airline_account = "pers"
    airline_company = "wn"
    create_var = locals()
    scraper = create_var[airline_account.capitalize() + airline_company.upper() + "Scraper"]()  # 声明下单类
    result = scraper.process_to_main(1111, "test.log", post_data, False, "http://127.0.0.1:8888")

    # time.sleep(2)

