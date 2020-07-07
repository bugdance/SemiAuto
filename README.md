Selenium 去除windows下运行driver的cmd命令框
Python下subprocess.popen()

self.process = subprocess.Popen(cmd, env=self.env,
                                close_fds=platform.system() != 'Windows',
                                stdout=self.log_file,
                                stderr=self.log_file,
                                stdin=PIPE, creationflags=134217728)





要解决的问题：
已解决
1.浏览器黑框  已解决
2.搜索或者筛选
3.滚动条
4.单元格展示
5.下单返回失败
6.订单号复制
7.状态实时刷新
8.锁单下单合并
9.关闭浏览器

未解决
1.禁用输入法
2.32位系统打包
3.刷新提醒


Python3.7.3  pyqt5  requests

Python build_pyd.py build


Name:QtDesigner 
Group:Qt 
Programs:F:\anaconda\Library\bin\designer.exe(这里是各位自己的designer路径，之前所看到的) 
Working directory：$ProjectFileDir$ 

Name:Pyuic 
Group:Qt 
Program:F:\anaconda\python.exe(各位自己的python路径) 
Arguments：-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py 
Working directory：$FileDir$ 