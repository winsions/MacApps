# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-12-13 19:11:09

import os
from datetime import datetime
import time
import os
import string


work_dir = os.getcwd()
os.system("cd ..")
file_path = os.path.join(os.getcwd(), "..")
os.chdir(file_path)

os.system("git clone http://203.60.2.120:9900/bbsport-ios/bbsport-ios.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/basebusinesscomponent.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/utilitytoolcomponentoc.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/utilitytoolcomponentswift.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/routercomponent.git")
os.system("git clone http://203.60.2.120:9900/ios/stuikit.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/homepagecomponent.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/loginregistercompoment.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/sportcomponent.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/userinfocomponentswift.git")
os.system("git clone http://203.60.2.120:9900/bbsport-ios/uicomponent.git")


# os.system("git clone ")



workList = []
# 获取文件夹
work_dir = os.getcwd()
path = os.listdir(work_dir)
for p in path:
	if os.path.isdir(p):
		if p.find("Python"):
			workList.append(p)
		else:
			print(p)
for x in workList:
	file_path = os.path.join(work_dir, x) # 拼接完整的路径
	print(file_path)
	os.chdir(file_path)
	os.system("git checkout" + " " + "develop")


# 进入主工程  pod install
file_path = os.path.join(work_dir, "zhugongcheng") # 拼接完整的路径
os.chdir(file_path)
os.system('pod install')
os.system('open BBSport.xcworkspace')
print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
os.chdir(work_dir)






