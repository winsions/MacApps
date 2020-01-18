# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-12-13 19:50:16

##发版打合并 在dev分支  打tag,然后合并dev分支到master分支


import os
import subprocess

tagBranch = raw_input("请输入tag的版本号:")

currentBranch = "master"

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


for x in workList:
	print(work_dir)
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)
	result = os.system("git status")

	os.system("git checkout" + " " + currentBranch)
	os.system("git pull origin" + " " + currentBranch)
	
	os.system('git tag ' + tagBranch)
	os.system('git push  --tags')

