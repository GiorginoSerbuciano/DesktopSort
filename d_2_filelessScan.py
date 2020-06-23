import os
import shutil

tagList = ['A_','B_','C_']

fileDir = 'Files'
fileList = os.scandir(fileDir)
nameList = []

for item in fileList:
	if item.is_file():
		nameList.append(item.name)
		print(item.name)
	elif item.is_dir() and item.name != tagList[0] and item.name != tagList[1]  and item.name != tagList[2]:
		nameList.append(item.name)
		print(item.name)

for fileName in nameList:
	if fileName.__contains__('A_'):
		shutil.move('Files/%s' %(fileName), 'Files/A_/%s' %(fileName))
	elif fileName.__contains__('B_'):
		print(fileName)
		shutil.move('Files/%s' %(fileName), 'Files/B_/%s' %(fileName))
	elif fileName.__contains__('C_'):
		print(fileName)
		shutil.move('Files/%s' %(fileName), 'Files/C_/%s' %(fileName))
