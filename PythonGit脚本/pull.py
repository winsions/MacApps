# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-12-13 19:42:12

import os

currentBranch = raw_input("请输入当前分支名:")
statusBranch = raw_input("请输入当前目标分支名:")
if len(currentBranch) == 0:
	currentBranch = "winsion"
if len(statusBranch) == 0:
	statusBranch = "develop"

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

for x in workList:
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)
	os.system("git status")

	os.system("git add .")
	os.system("git stash")

	os.system("git checkout" + " " + statusBranch)
	os.system("git pull origin" + " " + statusBranch)

	os.system("git checkout" + " " + currentBranch)
	os.system("git rebase" + " " + statusBranch)
	os.system('git stash pop')


# 进入主工程  pod install
file_path = os.path.join(work_dir, "zhugongcheng") # 拼接完整的路径
os.chdir(file_path)
os.system('pod install')
os.system('open BBSport.xcworkspace')



