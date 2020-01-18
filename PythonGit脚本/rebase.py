# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-12-13 19:40:55

import os

currentBranch = raw_input("请输入目标分支名称:")
statusBranch = raw_input("请输入基础分支名rebase代码,如果不输入表示只切换目标分支:")

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

print(workList)
for x in workList:
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)

	if len(statusBranch) != 0:

		os.system("git checkout" + " " + statusBranch)

		os.system("git pull origin" + " " + statusBranch)

	os.system("git checkout" + " " + currentBranch)

	if len(statusBranch) != 0:

		os.system("git rebase" + " " + statusBranch)

		os.system('git push origin ' + currentBranch)
	


