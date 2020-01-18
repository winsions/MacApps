# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-10-24 17:32:36

import os
import subprocess

currentBranch = input("请输入要推送的分支名:")
if len(currentBranch) == 0:
	currentBranch = "winsion"

work_dir = os.getcwd()

list1 = ['basebusinesscomponent', 'homepagecomponent', 'loginregistercompoment-', 'routercomponent', 'sportcomponent', 'userinfocomponent', 'utilitytoolcomponentoc',
 'utilitytoolcomponentswift', 'walletcomponent']
changeList = []
for x in list1:
	print(work_dir)
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)
	result = os.system("git status")

	os.system("git checkout" + " " + currentBranch)
	os.system("git pull origin" + " " + currentBranch)
	message = input('库:' + x + '输入修改的内容(默认:fixBug) :')
	if len(message) == 0:
		message = "fixBug"
	else:
		changeList.append(x)
	os.system('git add .')
	os.system("git commit -m " + message)
	os.system('git push origin ' + currentBranch)

print(changeList)
