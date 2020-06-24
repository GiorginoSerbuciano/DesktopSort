import os
import shutil

tagList = ['A_','B_','C_']

fileDir = 'Files'
fileList = os.scandir(fileDir)
nameList = [] #this list is read for the file names scanned in os.scandir(fileDir)

for item in fileList: #for every item resulting from os.scandir(fileDir)...
	if item.is_file(): 
		nameList.append(item.name)
		print(item.name) #testing feature
	elif item.is_dir() and item.name not in tagList: #if the destination folder is in the source folder and has the same name as its tag, the program will try to move it into itself, throwing up an error.
		nameList.append(item.name)
		print(item.name) #testing feature

for fileName in nameList: #reads every item in the list defined at the top
	if fileName.__contains__('A_'): #tags and directories should be user-definable without having to edit the source code
		shutil.move('Files/%s' %(fileName), 'Files/A_/%s' %(fileName))
	elif fileName.__contains__('B_'): #the program should check filenames for as many tags as there are tags; therefore, it should be able to 'generate' an elif (or something similar) for every tag.
		print(fileName) #testing feature
		shutil.move('Files/%s' %(fileName), 'Files/B_/%s' %(fileName))
	elif fileName.__contains__('C_'): 
		print(fileName) #testing feature
		shutil.move('Files/%s' %(fileName), 'Files/C_/%s' %(fileName))
