# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-12-06 14:32:33

import os

currentBranch = raw_input("请输入目标分支名称:")
statusBranch = raw_input("请输入基础分支名rebase代码,如果不输入表示只切换目标分支:")

work_dir = os.getcwd()

list1 = ['basebusinesscomponent', 'homepagecomponent', 'loginregistercompoment-', 'routercomponent', 'sportcomponent',  'userinfocomponent', 'utilitytoolcomponentoc',
 'utilitytoolcomponentswift', 'walletcomponent']
for x in list1:
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)

	if len(statusBranch) != 0:

		os.system("git checkout" + " " + statusBranch)

		os.system("git pull origin" + " " + statusBranch)

	os.system("git checkout" + " " + currentBranch)

	if len(statusBranch) != 0:

		os.system("git merge" + " " + statusBranch)

		os.system('git push origin ' + currentBranch)
	


