import os
import shutil
		
desktop = "C:/Users/Serban/Desktop"
scan = os.scandir(desktop)
tag = 'scan'
nameList = []

for item in scan:
	if item.is_dir() or item.is_file():
		nameList.append(item.name)
		print(item.name)
print (nameList)
for filename in nameList:
	if filename.__contains__('scan'):
		print(filename)
		#shutil.move('/Users/Serban/Desktop/%' %(filename), '/Users/Serban/Desktop/SORT/%' %(filename))
		shutil.move('/Users/Serban/Desktop/%s' %(filename), '/Users/Serban/Desktop/SORT/%s' %(filename))

