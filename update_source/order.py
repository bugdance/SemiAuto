#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019

written by pyleo.
"""

# =========================重点改地址=============================
from . import settings
# from source.browser import Browser
from assistant.update_source.browser import Browser
# ==================================================================
from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import threading


class OrderWindow(QtWidgets.QMainWindow):
    """表格窗口

    """
    
    def __init__(self, order_window: object=None, current_version: str=None, args: list=None) -> None:
        """
        
        :param main_window:
        :param args: 登录信息 [公司，用户名，密码，登录用户id]
        """
        super(OrderWindow, self).__init__()
        self._main_window = order_window
        self._main_ui = None
        self._current_version = current_version
        self._args = args
        self._translate = QtCore.QCoreApplication.translate
        self._query_time = QTimer(self)  # 查询数据定时器
        self._count = settings.TIME_COUNT            # 等待最大计数
        #################################################################
        self._query_data = None  # 查询的数据
        self.scramble_window = None
        self.scramble_ui = None
        #################################################################
        self._central_widget = None         # 面板
        self._group_box = None
        self._table_widget = None             # 标签
        self._query_button = None
        self._condition_combo = None
        self._search_edit = None
        self._search_button = None           # 进度条
        self._status_bar = None
        
    def order_setup(self) -> None:
        """表格设置

        :return: None
        """
        # # # 程序主窗口，图标，地址源
        self._main_window.setObjectName("order_window")
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
        icon.addPixmap(QtGui.QPixmap("source/fire.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._change_button.setIcon(icon)
        self._change_button.setIconSize(QtCore.QSize(24, 24))
        self._change_button.setCheckable(False)
        self._change_button.setFlat(False)
        self._change_button.setObjectName("change_button")
        
        self._query_button = QtWidgets.QPushButton(self._central_widget)
        self._query_button.setGeometry(QtCore.QRect(200, 15, 140, 35))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/refresh.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._query_button.setIcon(icon)
        self._query_button.setIconSize(QtCore.QSize(24, 24))
        self._query_button.setCheckable(False)
        self._query_button.setFlat(False)
        self._query_button.setObjectName("query_button")

        self._condition_combo = QtWidgets.QComboBox(self._central_widget)
        self._condition_combo.setGeometry(QtCore.QRect(400, 15, 140, 35))
        self._condition_combo.setObjectName("condition_combo")
        
        self._search_edit = QtWidgets.QLineEdit(self._central_widget)
        self._search_edit.setGeometry(QtCore.QRect(550, 15, 160, 35))
        self._search_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._search_edit.setInputMask("")
        self._search_edit.setMaxLength(30)
        self._search_edit.setCursorPosition(0)
        self._search_edit.setAlignment(QtCore.Qt.AlignLeft)
        self._search_edit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self._search_edit.setClearButtonEnabled(False)
        self._search_edit.setObjectName("search_edit")

        self._search_button = QtWidgets.QPushButton(self._central_widget)
        self._search_button.setGeometry(QtCore.QRect(730, 15, 140, 35))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._search_button.setIcon(icon)
        self._search_button.setIconSize(QtCore.QSize(24, 24))
        self._search_button.setCheckable(False)
        self._search_button.setFlat(False)
        self._search_button.setObjectName("search_button")

        self._status_bar = QtWidgets.QStatusBar(self._main_window)
        self._status_bar.setObjectName("status_bar")
        self._main_window.setStatusBar(self._status_bar)
        self._main_window.setCentralWidget(self._central_widget)
        # # # 写入内容
        self._main_window.setWindowTitle(self._translate("order_window", f"航天华有 东风1号 {self._current_version}"))
        self._group_box.setTitle("")
        self._group_box.setStyleSheet("")
        
        self._table_widget.setColumnCount(8)
        titles = ['OTA订单号', '航司', '行程类型', '航班号', ' 平台订单状态', '订单日期', '任务状态', '操作']
        self._table_widget.setHorizontalHeaderLabels(titles)
        for i in range(len(titles)):
            self._table_widget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
            head_item = self._table_widget.horizontalHeaderItem(i)
            head_item.setForeground(QColor(200, 111, 30))  # 设置文字颜色
            
        self._change_button.setText(self._translate("change_button", "切换压位下单"))
        self._change_button.setStyleSheet(
            "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #87843b;"
            "border-style:none;border:1px solid #87843b;padding:1px;min-height:5px;border-radius:10px;")
            
        self._query_button.setText(self._translate("query_button", "刷新订单"))
        self._query_button.setStyleSheet(
            "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #1ab394;"
            "border-style:none;border:1px solid #1ab394;padding:1px;min-height:5px;border-radius:10px;")
        
        conditions = ['按订单号查询', '按某航司查询', '按锁定人查询']
        self._condition_combo.addItems(conditions)
        self._condition_combo.setStyleSheet("font: 14pt '楷体';")
        self._search_edit.setPlaceholderText(self._translate("search_edit", "最大字符数30"))
        self._search_button.setText(self._translate("search_button", "查  询"))
        self._search_button.setStyleSheet(
            "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #CDC5BF;"
            "border-style:none;border:1px solid #CDC5BF;padding:1px;min-height:5px;border-radius:10px;")
        self._search_button.setEnabled(False)
        # # # 加载动作
        self._change_button.clicked.connect(self.change_action)
        self._query_time.timeout.connect(self.query_count)
        self._query_button.clicked.connect(self.query_action)
        self._search_button.clicked.connect(self.query_search)
        self._table_widget.itemDoubleClicked.connect(self.copy_item)
        
        QtCore.QMetaObject.connectSlotsByName(self._main_window)

    def change_action(self) -> None:
        """复制单元格数据

        :return: None
        """
        # =========================重点改地址=============================
        # from source.scramble import ScrambleWindow
        from assistant.update_source.scramble import ScrambleWindow
        # ==================================================================
        self._main_window.close()
        self._main_window = QtWidgets.QMainWindow()
        self._main_ui = ScrambleWindow(self._main_window, self._current_version, self._args)
        self._main_ui.scramble_setup()
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
            self._query_button.setText(str(self._count))
            self._count -= 1
        else:
            self._query_time.stop()
            self._query_button.setEnabled(True)
            self._query_button.setText(self._translate("query_button", "订单信息"))
            self._query_button.setStyleSheet(
                "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #1ab394;"
                "border-style:none;border:1px solid #1ab394;padding:1px;min-height:5px;border-radius:10px;")
            self._count = settings.TIME_COUNT
    
    def query_action(self) -> None:
        """查询动作

        :return: None
        """
        self._query_button.setEnabled(False)
        self._query_button.setStyleSheet(
            "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #CDC5BF;"
            "border-style:none;border:1px solid #CDC5BF;padding:1px;min-height:5px;border-radius:10px;")
        self._search_button.setEnabled(False)
        self._search_button.setStyleSheet(
            "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #CDC5BF;"
            "border-style:none;border:1px solid #CDC5BF;padding:1px;min-height:5px;border-radius:10px;")
        thread = QueryThread(self._args)
        thread.signal.connect(self.query_back)
        thread.start()
    
    def query_back(self, is_error: bool = None, message: str = None, get_data: list = None) -> None:
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
            self.query_load(get_data)
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
                status = "未知状态"
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
                
                self._table_widget.setCellWidget(i, 7, self.task_button(item, order_no, round_tag, lock_username, account_id, purchase_channel))
        except Exception as ex:
            QMessageBox.critical(self, "错误", f"解析数据列表有误{ex}", QMessageBox.Yes)
            self._status_bar.showMessage(self._translate("status_bar", "解析数据列表有误"))
            self._query_time.start(1000)
        else:
            self._status_bar.showMessage(self._translate("status_bar", "数据加载完成，欢迎使用小助手"))
            self._search_button.setStyleSheet(
                "font: 12pt '楷体';color: rgb(255, 255, 255);background-color: #1ab394;"
                "border-style:none;border:1px solid #1ab394;padding:1px;min-height:5px;border-radius:10px;")
            self._search_button.setEnabled(True)
            self._query_time.start(1000)
    
    def query_search(self) -> None:
        """搜索筛选数据
        
        :return: None
        """
        if self._search_edit.text() == "":
            QMessageBox.critical(self, "错误", f"条件不能为空", QMessageBox.Yes)
        else:
            try:
                col_condition = ""
                if "订单号" in self._condition_combo.currentText():
                    col_condition = "purchaseOrderNo"
                elif "航司" in self._condition_combo.currentText():
                    col_condition = "purchaseChannel"
                elif "锁定人" in self._condition_combo.currentText():
                    col_condition = "orderLockUserName"
                row = 0
                last_data = []  # 拆分数据，中转拆成两行
                for i, v in enumerate(self._query_data):
                    if v[col_condition] == self._search_edit.text():
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
                if row == 0:
                    QMessageBox.critical(self, "错误", "筛选不到您要求的订单", QMessageBox.Yes)
                    self._status_bar.showMessage(self._translate("status_bar", "找不到您搜索的数据"))
                else:
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
                        status = "未知状态"
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
                
                        self._table_widget.setCellWidget(i, 7, self.task_button(item, order_no, round_tag, lock_username, account_id, purchase_channel))
                    self._status_bar.showMessage(self._translate("status_bar", "筛选加载完成，欢迎使用小助手"))
            except Exception as ex:
                QMessageBox.critical(self, "错误", f"筛选数据列表有误{ex}", QMessageBox.Yes)
                self._status_bar.showMessage(self._translate("status_bar", "筛选数据列表有误"))
                
    def task_button(self, item, order_no, round_tag, lock_username, account_id, purchase_channel) -> None:
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
        for i in settings.ORDER_COMPANY:
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
                    order_btn.clicked.connect(lambda: self.order_action(order_no, round_tag, purchase_channel, item, order_btn, close_btn))
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
                order_btn.clicked.connect(lambda: self.order_action(order_no, round_tag, purchase_channel, item, order_btn, close_btn))
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
    
    def order_action(self, order_no, round_tag, purchase_channel, item, order_btn, close_btn):
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
        order_data = [self._args[0], self._args[1], self._args[2], order_no, round_tag, purchase_channel, item, order_btn, close_btn, order_time]
        thread = OrderThread(order_data)
        thread.signal.connect(self.order_back)
        thread.start()
    
    def order_back(self, is_error: bool = None, message: str = None, order_no: str=None, round_tag: int=None,
                   item: object = None, order_btn: object = None, close_btn: object = None, order_time: object=None, browser: object = None):
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
                   order_btn: object=None, is_retry: bool=None):
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
            close_btn.setEnabled(False)
            close_btn.setText("下单完成")
            close_btn.setStyleSheet("color: rgb(255, 255, 255);background-color: #FF0000;")
            item.setFont(QFont("song", 10, QFont.Bold))
            item.setForeground(QBrush(QColor("#FF0000")))


class QueryThread(QThread):
    """检查子线程类

    """
    signal = pyqtSignal(bool, str, list)  # 回调参数
    
    def __init__(self, args) -> None:
        super(QueryThread, self).__init__()
        self._args = args  # [公司， 账户名，密码]
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
        get_data = []
        try:
            post_data = f"companyFlag={self._args[0]}&loginName={self._args[1]}&password={self._args[2]}"
            response = requests.post(settings.LOGIN_URL, params=post_data, timeout=10)
            response.encoding = "utf-8"
        except Exception as ex:
            self._is_error = True
            self._message = f"{ex}"
        else:
            if response.status_code == 200 and response:
                try:
                    get_json = response.json()
                    msg = get_json['msg']
                    get_data = get_json['data']
                except Exception as ex:
                    self._is_error = True
                    self._message = f"解析返回数据有误{ex}"
                else:
                    if "成功" in msg:
                        self._is_error = False
                        self._message = msg
                    else:
                        self._is_error = True
                        self._message = msg
            else:
                self._is_error = True
                self._message = "请求服务不能返回数据,请联系管理员"
        self.signal.emit(self._is_error, self._message, get_data)  # 发射信号


class OrderThread(QThread):
    """检查线程类

    """
    signal = pyqtSignal(bool, str, str, int, object, object, object, object, object)  # 回调参数
    
    def __init__(self, args) -> None:
        super(OrderThread, self).__init__()
        self._args = args  # [公司， 账户名，密码, 订单号，单程标识, 航司二字码，标签，下单按钮，关闭按钮, 计时器]
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
        try:
            post_data = f"companyFlag={self._args[0]}&loginName={self._args[1]}" \
                f"&password={self._args[2]}&orderNo={self._args[3]}&roundTag={self._args[4]}"
            response = requests.post(settings.LOCK_URL, params=post_data, timeout=5)
            response.encoding = "utf-8"
        except Exception as ex:
            self._is_error = True
            self._message = f"{ex}"
        else:
            if response.status_code == 200 and response:
                try:
                    get_json = response.json()
                    msg = get_json['msg']
                    get_data = get_json['data']
                    if not get_data:
                        get_data = {}
                except Exception as ex:
                    self._is_error = True
                    self._message = f"解析返回数据有误{ex}"
                else:
                    if "SUCCESS" in msg:
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
                    else:
                        self._is_error = True
                        self._message = msg
            else:
                self._is_error = True
                self._message = "请求下单参数不能返回数据,请联系管理员"
        self.signal.emit(self._is_error, self._message, self._args[3], self._args[4], self._args[6], self._args[7], self._args[8], self._args[9], browser)  # 发射信号
        

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
