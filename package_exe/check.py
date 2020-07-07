#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019

written by pyleo.
"""

# ==========================可能要打包的第三方环境都预写在这里============================
from selenium import webdriver
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import requests
import threading
import configparser
import xlrd
# ========================================================================================


class CheckWindow(QtWidgets.QMainWindow):
    """检查主窗口

    """
    
    def __init__(self, check_window: object=None) -> None:
        """
        
        :param check_window:
        """
        super(CheckWindow, self).__init__()
        self._main_window = check_window            # 登录窗口实例
        self._main_ui = None                        # 登录配置
        self._translate = QtCore.QCoreApplication.translate
        self._check_time = QTimer(self)                             # 检查定时器
        self._config = configparser.ConfigParser()                 # 配置文件
        #################################################################
        self._version = None                                        # 本地配置大版本号
        self._edition = None                # 本地配置小版本号
        self._update_files = None           # 服务器上获取到的更新文件列表
        self._update_num = 0                # 更新进度
        self._add_num = 0                   # 累加进度
        self._update_version = None         # 服务器上获取到的大版本号
        self._update_edition = None         # 服务器上获取到的小版本号
        #################################################################
        self._central_widget = None         # 面板
        self._main_label = None             # 标签
        self._progress_bar = None           # 进度条
        
    def check_setup(self) -> None:
        """
        
        :return:
        """
        # # # 程序主窗口，图标，地址源
        self._main_window.setObjectName(f"check_window")
        self._main_window.resize(349, 92)
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
        self._main_label = QtWidgets.QLabel(self._central_widget)
        self._main_label.setGeometry(QtCore.QRect(10, 10, 331, 41))
        self._main_label.setObjectName("main_label")
        self._progress_bar = QtWidgets.QProgressBar(self._central_widget)
        self._progress_bar.setGeometry(QtCore.QRect(10, 50, 331, 23))
        self._progress_bar.setObjectName("progress_bar")
        self._main_window.setCentralWidget(self._central_widget)
        # # # 写入内容
        self._main_window.setWindowTitle(self._translate("check_window", "航天华有，商旅无忧"))
        self._main_label.setText(self._translate("main_label", "正在检查更新。。。。。"))
        self._main_label.setStyleSheet("font: 14pt '楷体';color: #1ab394;")
        self._progress_bar.setProperty("value", 0)
        # # # 加载动作
        self._check_time.setInterval(1)
        self._check_time.timeout.connect(self.check_action)
        self._check_time.start()
        
        QtCore.QMetaObject.connectSlotsByName(self._main_window)
 
    def check_action(self) -> None:
        """检查动作, 检查配置文件
        
        :return: None
        """
        try:
            self._check_time.stop()
            self._config.read("config.ini")
            self._version = self._config.defaults()['version']
            self._edition = self._config.defaults()['edition']
        except Exception as ex:
            QMessageBox.critical(self, "错误", f"{ex}", QMessageBox.Yes)
            if QMessageBox.Yes:
                sys.exit()
        else:
            check_url = ["http://116.62.51.105:8888/check_version/", self._version, self._edition]
            thread = CheckThread(check_url)
            thread.signal.connect(self.check_back)
            thread.start()
        
    def check_back(self, is_error: bool=None, message: str=None, version: str=None, edition: str=None, update_files: list=None) -> None:
        """检查任务子线程回调函数
        
        :param is_error: 是否返回错误 True 返回错误
        :param message: 返回消息
        :param version: 返回的大版本号
        :param edition: 返回的小版本号
        :param update_files: 返回的更新文件列表
        :return: None
        """
        if is_error:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            if QMessageBox.Yes:
                sys.exit()
        else:
            if "大版本更新" in message:
                QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
                if QMessageBox.Yes:
                    sys.exit()
            elif "小版本更新" in message:
                self._main_label.setText(self._translate("main_label", message))
                self._update_version = version
                self._update_edition = edition
                self._update_files = update_files
                self.update_action([0, self._update_files[0]])
            else:
                self._main_label.setText(self._translate("main_label", message))
                # ============================重点改地址==================================
                from source.login import LoginWindow
                # from assistant.update_source.login import LoginWindow
                # =========================================================================
                self._main_window.close()
                self._main_window = QtWidgets.QMainWindow()
                self._main_ui = LoginWindow(self._main_window, version+"."+edition)
                self._main_ui.login_setup()
                self._main_window.show()
                
    def update_action(self, args: list=None) -> None:
        """更新动作, 更新配置文件
        
        :return: None
        """
        self._add_num = round(100/len(self._update_files), 2)       # 累加基础数值为 100除以个数
        thread = UpdateThread(args)
        thread.signal.connect(self.update_back)
        thread.start()
        
    def update_back(self, is_error: bool=None, message: str=None, index: int=None, update_file: str=None):
        """更新任务子线程回调函数
        
        :param is_error: 是否返回错误 True 返回错误
        :param message: 返回消息
        :param index: 更新文件得索引
        :param update_file: 更新的文件名字
        :return: None
        """
        self._update_num += self._add_num   # 更新进度累加
        if is_error:
            self.write_config()     # 重新配置文件
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            if QMessageBox.Yes:
                sys.exit()
        else:
            self._main_label.setText(self._translate("main_label", message))
            self._progress_bar.setValue(self._update_num)
            # # # 循环更新，如果更新到最后一个文件
            if update_file == self._update_files[-1]:
                self._config.defaults()['version'] = self._update_version
                self._config.defaults()['edition'] = self._update_edition
                self.write_config()                                             # 写入最新的配置信息
                self._main_label.setText(self._translate("main_label", "恭喜，更新成功"))
                self._progress_bar.setValue(100)
                # ============================重点改地址==================================
                from source.login import LoginWindow
                # from assistant.update_source.login import LoginWindow
                # =========================================================================
                self._main_window.close()
                self._main_window = QtWidgets.QMainWindow()
                self._main_ui = LoginWindow(self._main_window, self._update_version+"."+self._update_edition)
                self._main_ui.login_setup()
                self._main_window.show()
            else:
                # # # 继续更新下一个文件
                self.update_action([index+1, self._update_files[index+1]])

    def write_config(self) -> None:
        """写入最新配置文件
        
        :return: None
        """
        try:
            with open("config.ini", "w") as f:
                self._config.write(f)
        except Exception as ex:
            QMessageBox.critical(self, "错误", f"{ex}", QMessageBox.Yes)
            if QMessageBox.Yes:
                sys.exit()
        else:
            pass


class CheckThread(QThread):
    """检查子线程类

    """
    signal = pyqtSignal(bool, str, str, str, list)  # 回调参数
    
    def __init__(self, args) -> None:
        super(CheckThread, self).__init__()
        self._args = args  # [check_url, version, edition]
        self._is_error = False
        self._message = "未知错误"
    
    def __del__(self) -> None:
        self.wait()
    
    def run(self) -> None:
        """任务函数

        :return: None
        """
        threading.Thread(target=self.check_version).start()
    
    def check_version(self) -> None:
        """检查具体流程

        :return: None
        """
        version = ""
        edition = ""
        update_files = []
        try:
            post_json = {"version": self._args[1], "edition": self._args[2]}
            response = requests.post(self._args[0], json=post_json, timeout=5)
            response.encoding = "utf-8"
        except Exception as ex:
            self._is_error = True
            self._message = f"{ex}"
        else:
            if response.status_code == 200:
                try:
                    get_json = response.json()
                    is_success = get_json['success']
                    if is_success:
                        update_version = get_json['update_version']
                        update_edition = get_json['update_edition']
                        update_files = get_json['update_files']
                        version = get_json['version']
                        edition = get_json['edition']
                        if update_version:
                            self._is_error = False
                            self._message = f"大版本更新，请联系管理员"
                        elif update_edition:
                            self._is_error = False
                            self._message = f"小版本更新，需要更新配置"
                        else:
                            self._is_error = False
                            self._message = f"无版本更新，已是最新版本"
                    else:
                        self._is_error = True
                        self._message = f"比对版本错误"
                except Exception as ex:
                    self._is_error = True
                    self._message = f"{ex}"
                else:
                    pass
            else:
                self._is_error = True
                self._message = f"比对版本失败"
        self.signal.emit(self._is_error, self._message, version, edition, update_files)  # 发射信号


class UpdateThread(QThread):
    """更新具体流程

    """
    signal = pyqtSignal(bool, str, int, str)  # 回调参数
    
    def __init__(self, args: list=None) -> None:
        super(UpdateThread, self).__init__()
        self._args = args  # [索引，文件值]
        self._is_error = False
        self._message = "未知错误"
    
    def __del__(self) -> None:
        self.wait()
    
    def run(self) -> None:
        """任务函数

        :return: None
        """
        threading.Thread(target=self.update_file).start()
    
    def update_file(self) -> None:
        """更新具体流程
        
        :return:
        """
        try:
            response = requests.get("http://116.62.51.105:8888/download/"+self._args[1], timeout=5)
            response.encoding = "utf-8"
        except Exception as ex:
            self._is_error = True
            self._message = f"{ex}"
        else:
            if response.status_code == 200:
                try:
                    with open(f"source/{self._args[1]}", 'wb') as f:
                        f.write(response.content)
                except Exception as ex:
                    self._is_error = True
                    self._message = f"{ex}"
                else:
                    self._is_error = False
                    self._message = f"更新{self._args[1]}成功"
            else:
                self._is_error = True
                self._message = f"更新失败:{self._args[1]}可能丢失，请联系管理员"
        self.signal.emit(self._is_error, self._message, self._args[0], self._args[1])  # 发射信号


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_ui = CheckWindow(main_window)
    main_ui.check_setup()
    main_window.show()
    sys.exit(app.exec_())
