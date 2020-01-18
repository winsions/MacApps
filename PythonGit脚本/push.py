# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-12-13 19:48:42

import os
import subprocess

currentBranch = raw_input("请输入要推送的分支名:")
if len(currentBranch) == 0:
	currentBranch = "winsion"

# 获取路径
work_dir = os.getcwd()
os.system("cd ..")
file_path = os.path.join(os.getcwd(), "..")
os.chdir(file_path)

work_dir = os.getcwd()

workList = []
noList = ["Python","zhugongcheng"]

# 获取文件夹
work_dir = os.getcwd()
path = os.listdir(work_dir)
for p in path:
	if os.path.isdir(p):
		if p not in noList:
			print("222" + p)
			workList.append(p)

changeList = []
for x in workList:
	print(work_dir)
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)
	result = os.system("git status")

	os.system("git checkout" + " " + currentBranch)
	os.system("git pull origin" + " " + currentBranch)
	message = raw_input("库:" + x + "输入修改的内容(默认:fixBug) :")
	if len(message) == 0:
		message = "fixBug"
	else:
		changeList.append(x)
	os.system('git add .')
	os.system("git commit -m " + message)
	os.system('git push origin ' + currentBranch)

print(changeList)
