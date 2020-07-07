#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019

written by pyleo.
"""

# =========================重点改地址=============================
from . import settings
from source.browser import Browser
# from assistant.update_source.browser import Browser
# ==================================================================
from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import requests
import threading
import xlrd


class ScrambleWindow(QtWidgets.QMainWindow):
    """表格窗口

    """
    
    def __init__(self, scramble_window: object = None, current_version: str=None, args: list=None) -> None:
        """

        :param main_window:
        :param args: 登录信息 [公司，用户名，密码，登录用户id]
        """
        super(ScrambleWindow, self).__init__()
        self._main_window = scramble_window
        self._main_ui = None
        self._current_version = current_version
        self._args = args
        self._translate = QtCore.QCoreApplication.translate
        self._query_time = QTimer(self)  # 查询数据定时器
        self._count = settings.TIME_COUNT  # 等待最大计数
        #################################################################
        self._query_data = None  # 查询的数据
        #################################################################
        self._central_widget = None  # 面板
        self._group_box = None
        self._table_widget = None  # 标签
        self._upload_button = None
        
        self._status_bar = None
    
    def scramble_setup(self) -> None:
        """表格设置

        :return: None
        """
        # # # 程序主窗口，图标，地址源
        self._main_window.setObjectName("scramble_window")
        self._main_window.resize(921, 451)
        self._main_window.setFixedSize(self._main_window.width(), self._main_window.height())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._main_window.setWindowIcon(icon)
        self._main_window.setWindowOpacity(1.0)
        self._main_window.setStyleSheet("")
        self._main_window.setIconSize(QtCore.QSize(24, 24))
        # # # 面板布局
        self._central_widget = QtWidgets.QWidget(self._main_window)
        self._central_widget.setObjectName("central_widget")
        self._group_box = QtWidgets.QGroupBox(self._central_widget)
        self._group_box.setGeometry(QtCore.QRect(20, 30, 881, 371))
        self._group_box.setObjectName("groupBox")
        self._table_widget = QtWidgets.QTableWidget(self._group_box)
        self._table_widget.setGeometry(QtCore.QRect(30, 30, 821, 311))
        self._table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self._table_widget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        # self._table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        self._table_widget.setSelectionMode(QTableWidget.SingleSelection)
        self._table_widget.setShowGrid(True)
        self._table_widget.setGridStyle(QtCore.Qt.SolidLine)
        self._table_widget.setObjectName("table_widget")
        self._table_widget.setAutoScroll(False)
        self._table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self._table_widget.horizontalHeader().setSortIndicatorShown(False)
        self._table_widget.horizontalHeader().setStretchLastSection(True)
        self._table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self._table_widget.verticalHeader().setVisible(False)
        self._table_widget.verticalHeader().setSortIndicatorShown(False)
        self._table_widget.verticalHeader().setStretchLastSection(False)
        self._table_widget.setSortingEnabled(False)
        
        self._change_button = QtWidgets.QPushButton(self._central_widget)
        self._change_button.setGeometry(QtCore.QRect(50, 15, 140, 35))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/normal.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._change_button.setIcon(icon)
        self._change_button.setIconSize(QtCore.QSize(24, 24))
        self._change_button.setCheckable(False)
        self._change_button.setFlat(False)
        self._change_button.setObjectName("change_button")
        
        self._upload_button = QtWidgets.QPushButton(self._central_widget)
        self._upload_button.setGeometry(QtCore.QRect(200, 15, 140, 35))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/upload.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._upload_button.setIcon(icon)
        self._upload_button.setIconSize(QtCore.QSize(24, 24))
        self._upload_button.setCheckable(False)
        self._upload_button.setFlat(False)
        self._upload_button.setObjectName("upload_button")
        
        self._status_bar = QtWidgets.QStatusBar(self._main_window)
        self._status_bar.setObjectName("status_bar")
        self._main_window.setStatusBar(self._status_bar)
        self._main_window.setCentralWidget(self._central_widget)
        # # # 写入内容
        self._main_window.setWindowTitle(self._translate("scramble_window", f"航天华有 东风1号 {self._current_version}"))
        self._group_box.setTitle("")
        self._group_box.setStyleSheet("")
        
        self._table_widget.setColumnCount(8)
        titles = ['OTA订单号', '航司', '行程类型', '航班号', ' 平台订单状态', '订单日期', '任务状态', '操作']
        self._table_widget.setHorizontalHeaderLabels(titles)
        for i in range(len(titles)):
            self._table_widget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
            head_item = self._table_widget.horizontalHeaderItem(i)
            head_item.setForeground(QColor(200, 111, 30))  # 设置文字颜色
        
        self._change_button.setText(self._translate("change_button", "切换正常下单"))
        self._change_button.setStyleSheet(
            "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #f05b72;"
            "border-style:none;border:1px solid #f05b72;padding:1px;min-height:5px;border-radius:10px;")
        
        self._upload_button.setText(self._translate("upload_button", "上传数据"))
        self._upload_button.setStyleSheet(
            "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #1ab394;"
            "border-style:none;border:1px solid #1ab394;padding:1px;min-height:5px;border-radius:10px;")

        # # # 加载动作
        self._change_button.clicked.connect(self.change_action)
        self._query_time.timeout.connect(self.query_count)
        self._upload_button.clicked.connect(self.upload_action)

        self._table_widget.itemDoubleClicked.connect(self.copy_item)
        
        QtCore.QMetaObject.connectSlotsByName(self._main_window)
    
    def change_action(self) -> None:
        """

        :return: None
        """
        # =========================重点改地址=============================
        from source.order import OrderWindow
        # from assistant.update_source.order import OrderWindow
        # ==================================================================
        self._main_window.close()
        self._main_window = QtWidgets.QMainWindow()
        self._main_ui = OrderWindow(self._main_window, self._current_version, self._args)
        self._main_ui.order_setup()
        self._main_window.show()
    
    def copy_item(self) -> None:
        """复制单元格数据

        :return: None
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self._table_widget.currentItem().text())
    
    def query_count(self) -> None:
        """查询按钮计时

        :return: None
        """
        if self._count > 0:
            self._upload_button.setText(str(self._count))
            self._count -= 1
        else:
            self._query_time.stop()
            self._upload_button.setEnabled(True)
            self._upload_button.setText(self._translate("query_button", "上传数据"))
            self._upload_button.setStyleSheet(
                "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #1ab394;"
                "border-style:none;border:1px solid #1ab394;padding:1px;min-height:5px;border-radius:10px;")
            self._count = settings.TIME_COUNT
    
    def upload_action(self) -> None:
        """查询动作

        :return: None
        """
        self._upload_button.setEnabled(False)
        self._upload_button.setStyleSheet(
            "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #CDC5BF;"
            "border-style:none;border:1px solid #CDC5BF;padding:1px;min-height:5px;border-radius:10px;")

        file_path, file_type = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "XLSX Files (*.xlsx);;XLS Files (*.xls)")
        if file_path == "":
            self._upload_button.setEnabled(True)
            self._upload_button.setStyleSheet(
                "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #1ab394;"
                "border-style:none;border:1px solid #1ab394;padding:1px;min-height:5px;border-radius:10px;")
            return
        thread = UploadThread(file_path)
        thread.signal.connect(self.upload_back)
        thread.start()
    
    def upload_back(self, is_error: bool = None, message: str = None, get_data: dict = None) -> None:
        """查询任务子线程回调函数

        :param is_error: 是否返回错误 True 返回错误
        :param message: 返回消息
        :param get_data: 返回登录数据
        :return: None
        """
        if is_error:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            self._status_bar.showMessage(self._translate("status_bar", "请求数据有误"))
            if QMessageBox.Yes:
                self._query_time.start(1000)
        else:
            self.query_load([get_data])
            self._query_data = get_data
    
    def query_load(self, get_data: list = None) -> None:
        """查询加载数据

        :param get_data: 得到的数据
        :return: None
        """
        try:
            row = 0
            last_data = []  # 拆分数据，中转拆成两行
            for i, v in enumerate(get_data):
                ######## ======================= 造数据
                ticket_time = datetime.now() - timedelta(hours=8)
                ticket_time = datetime.strftime(ticket_time, '%Y-%m-%dT%H:%M:%S.000+0000')
                order_time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
                v['generateOrderTime'] = ticket_time
                v['flightNums'] = v['flightNum']
                v['orderLockAccountId'] = self._args[3]
                v['purchaseOrderNo'] = f"scrambel{self._args[3]}time{order_time}"
                v['purchaseChannel'] = v['purchasingChannel']
                v['flightOrderType'] = 1
                v['systemOrderStatus'] = "自定义压单"
                v['orderLockUserName'] = ""
                ######## ==================================
                
                nums = v['flightNums'].split(",")
                if len(nums) > 1:
                    for j in range(len(nums)):
                        v['flightNums'] = nums[j]
                        v['roundTag'] = j + 1
                        copy_value = v.copy()
                        last_data.append(copy_value)
                    row += len(nums)
                else:
                    v['roundTag'] = 1
                    last_data.append(v)
                    row += 1
            self._table_widget.setRowCount(row)  # 写入实际行数
            # # # 合并同一订单
            for i in range(row):
                account_id = last_data[i]['orderLockAccountId']
                round_tag = last_data[i]['roundTag']
                
                order_no = last_data[i]['purchaseOrderNo']
                if i < row - 1 and order_no == last_data[i + 1]['purchaseOrderNo']:
                    self._table_widget.setSpan(i, 0, 2, 1)
                item = QTableWidgetItem(str(order_no))
                self._table_widget.setItem(i, 0, item)
                
                purchase_channel = last_data[i]['purchaseChannel']
                item = QTableWidgetItem(str(purchase_channel))
                self._table_widget.setItem(i, 1, item)
                
                order_type = last_data[i]['flightOrderType']
                single_type = "单程(去程)"
                if order_type == 3:
                    if round_tag == 1:
                        single_type = "往返(去程)"
                    else:
                        single_type = "往返(回程)"
                item = QTableWidgetItem(str(single_type))
                self._table_widget.setItem(i, 2, item)
                
                flight_nums = last_data[i]['flightNums']
                item = QTableWidgetItem(str(flight_nums))
                self._table_widget.setItem(i, 3, item)
                
                order_status = last_data[i]['systemOrderStatus']
                status = "自定义压单"
                for k, v in settings.ORDER_STATUS.items():
                    if str(order_status) == k:
                        status = v
                item = QTableWidgetItem(str(status))
                self._table_widget.setItem(i, 4, item)
                
                ticket_time = last_data[i]['generateOrderTime']
                ticket_time = datetime.strptime(ticket_time, '%Y-%m-%dT%H:%M:%S.000+0000')
                ticket_time = ticket_time + timedelta(hours=8)
                ticket_time = ticket_time.strftime("%Y-%m-%d %H:%M:%S")
                item = QTableWidgetItem(str(ticket_time))
                self._table_widget.setItem(i, 5, item)
                
                lock_username = last_data[i]['orderLockUserName']
                item = QTableWidgetItem(str(lock_username))
                self._table_widget.setItem(i, 6, item)
                self._table_widget.setCellWidget(i, 7, self.task_button(item, order_no, round_tag, lock_username, account_id, purchase_channel, last_data[i]))
        except Exception as ex:
            QMessageBox.critical(self, "错误", f"解析数据列表有误{ex}", QMessageBox.Yes)
            self._status_bar.showMessage(self._translate("status_bar", "解析数据列表有误"))
            self._query_time.start(1000)
        else:
            self._status_bar.showMessage(self._translate("status_bar", "数据加载完成，欢迎使用小助手"))
            self._query_time.start(1000)
    
    def task_button(self, item, order_no, round_tag, lock_username, account_id, purchase_channel, data_dict) -> None:
        """增加任务按钮

        :param item: 状态标签
        :param order_no: 订单号
        :param round_tag: 去程标识
        :param lock_username: 锁定人
        :param account_id: 锁定用户id
        :param purchase_channel: 航司二字码
        :return: None
        """
        widget = QWidget()
        order_btn = QPushButton()
        close_btn = QPushButton()
        close_btn.setVisible(False)
        is_order = 0
        for i in settings.SCRAMBLE_COMPANY:
            if i == purchase_channel:
                is_order = 1
                break
        if is_order:
            if lock_username:
                order_btn.setEnabled(False)
                item.setText(self._translate("item", lock_username))
                item.setFont(QFont("song", 10, QFont.Bold))
                item.setForeground(QBrush(QColor("#7B68EE")))
                if account_id == self._args[3] and "状态发生变化" not in lock_username:
                    order_btn.setEnabled(True)
                    order_btn.setText(self._translate("order_btn", "直接下单"))
                    order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #1ab394;")
                    item.setFont(QFont("song", 10, QFont.Bold))
                    item.setForeground(QBrush(QColor("#1ab394")))
                    order_btn.clicked.connect(lambda: self.order_action(order_no, round_tag, purchase_channel, item, order_btn, close_btn, data_dict))
                else:
                    order_btn.setEnabled(False)
                    order_btn.setText(self._translate("order_btn", "已被锁定"))
                    order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #7B68EE;")
                    item.setFont(QFont("song", 10, QFont.Bold))
                    item.setForeground(QBrush(QColor("#7B68EE")))
            else:
                order_btn.setEnabled(True)
                order_btn.setText(self._translate("order_btn", "锁单下单"))
                order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #1ab394;")
                item.setFont(QFont("song", 10, QFont.Bold))
                item.setForeground(QBrush(QColor("#1ab394")))
                order_btn.clicked.connect(lambda: self.order_action(order_no, round_tag, purchase_channel, item, order_btn, close_btn, data_dict))
        else:
            order_btn.setEnabled(False)
            order_btn.setText(self._translate("order_btn", "暂不支持"))
            order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #708090;")
            item.setFont(QFont("song", 10, QFont.Bold))
            item.setForeground(QBrush(QColor("#708090")))
        hLayout = QHBoxLayout()
        hLayout.addWidget(order_btn)
        hLayout.addWidget(close_btn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget
    
    def order_action(self, order_no, round_tag, purchase_channel, item, order_btn, close_btn, data_dict):
        """

        :return:
        """
        _count = 0
        
        def order_count() -> None:
            """查询按钮计时

            :return: None
            """
            nonlocal _count
            order_btn.setText(str(_count))
            _count += 1
        
        order_time = QTimer(self)  # 查询数据定时器
        order_time.timeout.connect(order_count)
        order_time.start(1000)
        
        order_btn.setEnabled(False)
        order_btn.setText("正在下单")
        order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #EEC900;")
        item.setFont(QFont("song", 10, QFont.Bold))
        item.setForeground(QBrush(QColor("#EEC900")))
        order_data = [self._args[0], self._args[1], self._args[2], order_no, round_tag, purchase_channel, item, order_btn, close_btn, order_time, data_dict]
        thread = OrderThread(order_data)
        thread.signal.connect(self.order_back)
        thread.start()
    
    def order_back(self, is_error: bool = None, message: str = None, order_no: str = None, round_tag: int = None,
                   item: object = None, order_btn: object = None, close_btn: object = None, order_time: object = None, browser: object = None):
        order_time.stop()
        if is_error:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            if QMessageBox.Yes:
                if "状态发生变化" in message:
                    order_btn.setEnabled(False)
                    order_btn.setText("已被锁定")
                    order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #7B68EE;")
                    item.setFont(QFont("song", 10, QFont.Bold))
                    item.setForeground(QBrush(QColor("#7B68EE")))
                    item.setText(message)
                    self.change_data(order_no, round_tag)
                elif "浏览器打开存在问题" in message:
                    order_btn.setEnabled(False)
                    order_btn.setVisible(False)
                    close_btn.setEnabled(True)
                    close_btn.setVisible(True)
                    close_btn.setText("关浏览器")
                    close_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #1C86EE;")
                    item.setFont(QFont("song", 10, QFont.Bold))
                    item.setForeground(QBrush(QColor("#1C86EE")))
                    close_btn.clicked.connect(lambda: self.close_action(item, close_btn, order_btn, browser, True))
                else:
                    order_btn.setText("重新下单")
                    order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #1C86EE;")
                    order_btn.setEnabled(True)
                    item.setFont(QFont("song", 10, QFont.Bold))
                    item.setForeground(QBrush(QColor("#1C86EE")))
        else:
            order_btn.setEnabled(False)
            order_btn.setVisible(False)
            close_btn.setEnabled(True)
            close_btn.setVisible(True)
            close_btn.setText("关浏览器")
            close_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #1C86EE;")
            item.setFont(QFont("song", 10, QFont.Bold))
            item.setForeground(QBrush(QColor("#1C86EE")))
            close_btn.clicked.connect(lambda: self.close_action(item, close_btn, order_btn, browser, False))
    
    def change_data(self, order_no, round_tag):
        """改变现有数据

        :return: None
        """
        for i, v in enumerate(self._query_data):
            if v['purchaseOrderNo'] == order_no and v['roundTag'] == round_tag:
                v['orderLockUserName'] = "状态发生变化"
    
    def close_action(self, item, close_btn, order_btn, browser, is_retry):
        """

        :return: None
        """
        close_btn.setEnabled(False)
        close_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #EEC900;")
        item.setFont(QFont("song", 10, QFont.Bold))
        item.setForeground(QBrush(QColor("#EEC900")))
        close_data = [item, close_btn, order_btn, browser, is_retry]
        thread = CloseThread(close_data)
        thread.signal.connect(self.close_back)
        thread.start()
    
    def close_back(self, is_error: bool = None, message: str = None, item: object = None, close_btn: object = None,
                   order_btn: object = None, is_retry: bool = None):
        if is_error:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
        if is_retry:
            order_btn.setEnabled(True)
            order_btn.setVisible(True)
            close_btn.setEnabled(False)
            close_btn.setVisible(False)
            order_btn.setText("重新下单")
            order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #1C86EE;")
            order_btn.setEnabled(True)
            item.setFont(QFont("song", 10, QFont.Bold))
            item.setForeground(QBrush(QColor("#1C86EE")))
        else:
            order_btn.setEnabled(True)
            order_btn.setVisible(True)
            close_btn.setEnabled(False)
            close_btn.setVisible(False)
            order_btn.setText("重新下单")
            order_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #1C86EE;")
            order_btn.setEnabled(True)
            item.setFont(QFont("song", 10, QFont.Bold))
            item.setForeground(QBrush(QColor("#1C86EE")))


class UploadThread(QThread):
    """检查子线程类

    """
    signal = pyqtSignal(bool, str, dict)  # 回调参数
    
    def __init__(self, path) -> None:
        super(UploadThread, self).__init__()
        self._path = path  # 文件地址
        self._is_error = False
        self._message = "未知错误"
    
    def __del__(self) -> None:
        self.wait()
    
    def run(self) -> None:
        """任务函数

        :return: None
        """
        threading.Thread(target=self.query_account).start()
    
    def query_account(self) -> None:
        """查询具体流程

        :return: None
        """
        get_data = {
            'departureTime': '', 'contactMobile': '13717573545', 'adultNum': 3, 'childNum': 0, 'contactEmail': '168033518@qq.com',
            'purchasingChannel': 'MM', 'flightType': '', 'userName': '168033518@qq.com', 'depDate': '2019-08-01', 'flightNum': 'VY9496',
            'password': 'Su123456', 'depAirCode': 'CDG', 'infantNum': 0, 'arrAircode': 'PRG', 'currency': 'THB', 'priceTax': 0, 'promo': '',
            'passengersDataList': [],
            'additionalServicesDataList': []}
        adult_num = 0
        child_num = 0
        try:
            with xlrd.open_workbook(self._path, encoding_override='utf-8') as x:  # 打开excel
                base_table = x.sheets()[0]
                passenger_table = x.sheets()[1]
            base_rows = base_table.nrows  # 获取行数
            passenger_rows = passenger_table.nrows
            for i in range(1, base_rows):  # 线程数一组
                excel_data = base_table.row_values(i)
                get_data['purchasingChannel'] = excel_data[0]
                get_data['depAirCode'] = excel_data[1]
                get_data['arrAircode'] = excel_data[2]
                get_data['flightNum'] = excel_data[3]
                get_data['depDate'] = excel_data[4]
                get_data['userName'] = excel_data[5]
                get_data['password'] = excel_data[6]
                get_data['contactMobile'] = excel_data[7]
                get_data['contactEmail'] = excel_data[8]
                get_data['currency'] = excel_data[9]
                get_data['promo'] = excel_data[10]
            for i in range(1, passenger_rows):  # 线程数一组
                excel_data = passenger_table.row_values(i)
                passenger_data = {'passengerName': 'ZHOU/RUNXIA', 'ageType': 0, 'birthday': '1994-11-11', 'gender': 'F',
                                  'cardNum': 'EF9244001',
                                  'cardType': 'PP', 'cardIssuePlace': 'CN', 'cardExpired': '2029-04-01',
                                  'nationality': 'CN'}
                passenger_data['passengerName'] = excel_data[0]+"/"+excel_data[1]
                passenger_data['gender'] = excel_data[2]
                passenger_data['birthday'] = excel_data[3]
                passenger_data['ageType'] = int(excel_data[4])
                if excel_data[4] == "0":
                    adult_num += 1
                elif excel_data[4] == "1":
                    child_num += 1
                passenger_data['cardNum'] = excel_data[5]
                passenger_data['cardExpired'] = excel_data[6]
                passenger_data['nationality'] = excel_data[7]
                get_data['passengersDataList'].append(passenger_data)
            get_data['adultNum'] = adult_num
            get_data['childNum'] = child_num
        except Exception as ex:
            self._is_error = True
            self._message = f"excel格式有误，请检查"
        else:
            pass
        self.signal.emit(self._is_error, self._message, get_data)  # 发射信号


class OrderThread(QThread):
    """检查线程类

    """
    signal = pyqtSignal(bool, str, str, int, object, object, object, object, object)  # 回调参数
    
    def __init__(self, args) -> None:
        super(OrderThread, self).__init__()
        self._args = args  # [公司， 账户名，密码, 订单号，单程标识, 航司二字码，标签，下单按钮，关闭按钮, 计时器, 请求数据]
        self._is_error = False
        self._message = "未知错误"
    
    def __del__(self) -> None:
        self.wait()
    
    def run(self):
        threading.Thread(target=self.order_query).start()
    
    def order_query(self):
        """

        :return: None
        """
        browser = None
        get_data = self._args[-1]
        try:
            url = ""
            for k, v in settings.ORDER_URL.items():
                if self._args[5].upper() == k.upper():
                    url = v
            get_data['orderNO'] = f"{self._args[3]}-{self._args[4]}"
            response = requests.post(url, json=get_data, timeout=60)
            response.encoding = "utf-8"
        except Exception as ex:
            self._is_error = True
            self._message = f"{ex}"
        else:
            if response.status_code == 200 and response:
                try:
                    get_json = response.json()
                    msg = get_json['msg']
                    cookie = get_json['cookie']
                    cookies = []
                    domain = ""
                    for k, v in settings.ORDER_PAY.items():
                        if self._args[5].upper() == k.upper():
                            domain = v[0]
                            url = v[1]
                    for k, v in cookie.items():
                        cookies.append({"name": k, "value": v, "domain": domain, "path": "/"})
                except Exception as ex:
                    self._is_error = True
                    self._message = f"解析返回数据有误{ex}"
                else:
                    if "成功" in msg:
                        browser = Browser()
                        result = browser.set_chrome()
                        if "成功" in result:
                            browser.set_url("https://www.baidu.com")
                            result = browser.set_cookies(cookies)
                            if "成功" in result:
                                result = browser.set_url(url)
                                if "成功" or "超时" in result:
                                    self._is_error = False
                                    self._message = "浏览器打开正常"
                                else:
                                    self._is_error = True
                                    self._message = "浏览器打开存在问题"
                            else:
                                self._is_error = True
                                self._message = "浏览器打开存在问题"
                        else:
                            self._is_error = True
                            self._message = "浏览器打开存在问题"
                    else:
                        self._is_error = True
                        self._message = msg
            else:
                self._is_error = True
                self._message = "请求服务不能返回数据,请联系管理员"
        self.signal.emit(self._is_error, self._message, self._args[3], self._args[4], self._args[6], self._args[7], self._args[8], self._args[9],
                         browser)  # 发射信号


class CloseThread(QThread):
    """检查线程类

    """
    signal = pyqtSignal(bool, str, object, object, object, bool)  # 回调参数
    
    def __init__(self, args) -> None:
        super(CloseThread, self).__init__()
        self._args = args  # [标签，关闭按钮, 下单按钮, 浏览器， 是否重新下单]
        self._is_error = False
        self._message = "未知错误"
    
    def __del__(self) -> None:
        self.wait()
    
    def run(self):
        """

        :return:
        """
        threading.Thread(target=self.close_driver).start()
    
    def close_driver(self):
        """

        :return:
        """
        result = self._args[3].set_quit()
        if "成功" in result:
            self._is_error = False
            self._message = "true"
        else:
            self._is_error = True
            self._message = result
        self.signal.emit(self._is_error, self._message, self._args[0], self._args[1], self._args[2], self._args[4])  # 发射信号
