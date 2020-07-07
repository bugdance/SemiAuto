#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019

written by pyleo.
"""

# =========================重点改地址=============================
from . import settings
# from source.order import OrderWindow
from assistant.update_source.order import OrderWindow
# ==================================================================
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import threading
        

class LoginWindow(QtWidgets.QMainWindow):
    """登录窗口

    """
    
    def __init__(self, login_window: object=None, current_version: str="") -> None:
        """
        
        :param login_window:
        :param current_version:
        """
        super(LoginWindow, self).__init__()
        self._main_window = login_window
        self._main_ui = None
        self._current_version = current_version
        self._translate = QtCore.QCoreApplication.translate
        self._login_time = QTimer(self)  # 登录定时器
        self._count = settings.TIME_COUNT            # 等待最大计数
        #################################################################
        self._order_window = None                    # 表格窗口
        self._order_ui = None                        # 表格配置
        #################################################################
        self._central_widget = None         # 面板
        self._group_box = None
        self._main_label = None             # 标签
        self._main_line = None
        self._company_edit = None
        self._account_edit = None           # 进度条
        self._passport_edit = None
        self._login_button = None
        
    def login_setup(self) -> None:
        """登录设置
        
        :return: None
        """
        # # # 程序主窗口，图标，地址源
        self._main_window.setObjectName("login_window")
        self._main_window.resize(391, 353)
        self._main_window.setFixedSize(self._main_window.width(), self._main_window.height())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._main_window.setWindowIcon(icon)
        self._main_window.setWindowOpacity(1.0)
        self._main_window.setStyleSheet("")
        self._main_window.setIconSize(QtCore.QSize(50, 50))
        # # # 面板布局
        self._central_widget = QtWidgets.QWidget(self._main_window)
        self._central_widget.setObjectName("central_widget")
        self._group_box = QtWidgets.QGroupBox(self._central_widget)
        self._group_box.setGeometry(QtCore.QRect(30, 30, 331, 101))
        self._group_box.setFocusPolicy(QtCore.Qt.TabFocus)
        self._group_box.setFlat(False)
        self._group_box.setObjectName("group_box")
        self._main_label = QtWidgets.QLabel(self._group_box)
        self._main_label.setGeometry(QtCore.QRect(50, 10, 241, 41))
        self._main_label.setAlignment(QtCore.Qt.AlignCenter)
        self._main_label.setObjectName("main_label")
        self._main_line = QtWidgets.QFrame(self._group_box)
        self._main_line.setGeometry(QtCore.QRect(20, 60, 291, 20))
        self._main_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self._main_line.setLineWidth(1)
        self._main_line.setFrameShape(QtWidgets.QFrame.HLine)
        self._main_line.setObjectName("main_line")
        
        self._company_edit = QtWidgets.QLineEdit(self._central_widget)
        self._company_edit.setGeometry(QtCore.QRect(30, 130, 331, 31))
        self._company_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._company_edit.setInputMask("")
        self._company_edit.setMaxLength(20)
        self._company_edit.setCursorPosition(0)
        self._company_edit.setAlignment(QtCore.Qt.AlignCenter)
        self._company_edit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self._company_edit.setClearButtonEnabled(False)
        self._company_edit.setObjectName("company_edit")
        self._account_edit = QtWidgets.QLineEdit(self._central_widget)
        self._account_edit.setGeometry(QtCore.QRect(30, 179, 331, 31))
        self._account_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._account_edit.setMaxLength(20)
        self._account_edit.setCursorPosition(0)
        self._account_edit.setAlignment(QtCore.Qt.AlignCenter)
        self._account_edit.setObjectName("account_edit")
        self._passport_edit = QtWidgets.QLineEdit(self._central_widget)
        self._passport_edit.setGeometry(QtCore.QRect(30, 229, 331, 31))
        self._passport_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._passport_edit.setMaxLength(20)
        self._passport_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self._passport_edit.setCursorPosition(0)
        self._passport_edit.setAlignment(QtCore.Qt.AlignCenter)
        self._passport_edit.setAttribute(QtCore.Qt.WA_InputMethodEnabled, False)
        self._passport_edit.setObjectName("passport_edit")
        
        self._login_button = QtWidgets.QPushButton(self._central_widget)
        self._login_button.setGeometry(QtCore.QRect(30, 280, 331, 41))
        self._login_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._login_button.setAutoDefault(False)
        self._login_button.setDefault(False)
        self._login_button.setObjectName("login_button")
        self._main_window.setCentralWidget(self._central_widget)
        # # # 写入内容
        self._main_window.setWindowTitle(self._translate("login_window", f"航天华有 东风1号 {self._current_version}"))
        self._group_box.setTitle("")
        self._group_box.setStyleSheet("")
        self._main_label.setText(self._translate("main_label", "让旅行更美好！"))
        self._main_label.setStyleSheet("font: 26pt '楷体';color: #1ab394;")
        self._main_line.setStyleSheet("")
        self._company_edit.setPlaceholderText(self._translate("company_edit", "请输入公司"))
        self._company_edit.setStyleSheet(
            "border-style:none;border:1px solid #000000;padding:1px;min-height:5px;border-radius:10px;")
        self._account_edit.setPlaceholderText(self._translate("account_edit", "请输入账号"))
        self._account_edit.setStyleSheet(
            "border-style:none;border:1px solid #000000;padding:1px;min-height:5px;border-radius:10px;")
        self._passport_edit.setPlaceholderText(self._translate("passport_edit", "请输入密码"))
        self._passport_edit.setStyleSheet(
            "border-style:none;border:1px solid #000000;padding:1px;min-height:5px;border-radius:10px;")
        self._login_button.setText(self._translate("login_button", "登  录"))
        self._login_button.setStyleSheet(
            "font: 16pt '楷体';color: rgb(255, 255, 255);background-color: #1ab394;"
            "border-style:none;border:1px solid #1ab394;padding:1px;min-height:5px;border-radius:10px;")
        self._login_button.setShortcut(self._translate("login_button", "return"))
        # # # 加载动作
        self._login_button.clicked.connect(self.login_action)
        self._login_time.setInterval(1000)
        self._login_time.timeout.connect(self.login_count)
        
        QtCore.QMetaObject.connectSlotsByName(self._main_window)
        self._main_window.setTabOrder(self._group_box, self._company_edit)
        self._main_window.setTabOrder(self._company_edit, self._account_edit)
        self._main_window.setTabOrder(self._account_edit, self._passport_edit)
        self._main_window.setTabOrder(self._passport_edit, self._login_button)

    def login_count(self) -> None:
        """登录按钮计时

        :return: None
        """
        if self._count > 0:
            self._login_button.setText(str(self._count))
            self._count -= 1
        else:
            self._login_time.stop()
            self._login_button.setEnabled(True)
            self._login_button.setText(self._translate("login_button", "登  录"))
            self._login_button.setShortcut(self._translate("login_button", "return"))
            self._login_button.setStyleSheet(
                "font: 16pt '楷体';color: rgb(255, 255, 255);background-color: #1ab394;"
                "border-style:none;border:1px solid #1ab394;padding:1px;min-height:5px;border-radius:10px;")
            self._count = settings.TIME_COUNT

    def login_action(self) -> None:
        """登录动作
        
        :return: None
        """
        if self._company_edit.text() == "" or self._account_edit.text() == "" or self._passport_edit.text() == "":
            QMessageBox.warning(self, "警告", "请您把信息填全！", QMessageBox.Yes)
        else:
            self._login_button.setEnabled(False)
            self._login_button.setStyleSheet(
                "font: 16pt '楷体';color: rgb(255, 255, 255);background-color: #CDC5BF;"
                "border-style:none;border:1px solid #CDC5BF;padding:1px;min-height:5px;border-radius:10px;")
            login_data = [self._company_edit.text(), self._account_edit.text(), self._passport_edit.text()]
            thread = LoginThread(login_data)
            thread.signal.connect(self.login_back)
            thread.start()
        
    def login_back(self, is_error: bool=None, message: str=None, args: list=None) -> None:
        """登录任务子线程回调函数
        
        :param is_error: 是否返回错误 True 返回错误
        :param message: 返回消息
        :param args: # 返回的登录信息 [公司， 账户名，密码]
        :return: None
        """
        if is_error:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            if QMessageBox.Yes:
                self._login_time.start()
        else:
            self._main_window.close()
            self._main_window = QtWidgets.QMainWindow()
            self._main_ui = OrderWindow(self._main_window, self._current_version, args)
            self._main_ui.order_setup()
            self._main_window.show()


class LoginThread(QThread):
    """登录子线程类
    
    """
    signal = pyqtSignal(bool, str, list)                   # 括号里填写信号传递的参数

    def __init__(self, args: list=None) -> None:
        """
        
        :param args: [公司， 账户名，密码]
        """
        super(LoginThread, self).__init__()
        self._args = args
        self._is_error = False
        self._message = "未知错误"

    def __del__(self) -> None:
        self.wait()

    def run(self) -> None:
        """任务函数

        :return: None
        """
        threading.Thread(target=self.login_account).start()

    def login_account(self) -> None:
        """登录具体流程
        
        :return: None
        """
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
                except Exception as ex:
                    self._is_error = True
                    self._message = f"解析返回数据有误{ex}"
                else:
                    if "成功" in msg:
                        account_id = get_json['accountId']
                        self._args.append(account_id)         # 添加个值 [公司， 账户名，密码，账户id]
                        self._is_error = False
                        self._message = msg
                    else:
                        self._is_error = True
                        self._message = msg
            else:
                self._is_error = True
                self._message = "请求服务不能返回数据,请联系管理员"
        self.signal.emit(self._is_error, self._message, self._args)  # 发射信号
