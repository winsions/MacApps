# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-11-01 17:29:37

import os

currentBranch = input("请输入新分支名称:")
statusBranch = input("请输入基础分支名:")



work_dir = os.getcwd()

list1 = ['basebusinesscomponent', 'homepagecomponent', 'loginregistercompoment-', 'routercomponent', 'sportcomponent',  'userinfocomponent', 'utilitytoolcomponentoc',
 'utilitytoolcomponentswift', 'walletcomponent']
for x in list1:
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)
	os.system("git checkout -b " + currentBranch + " " + statusBranch)

	os.system("git push origin " + currentBranch)
	


