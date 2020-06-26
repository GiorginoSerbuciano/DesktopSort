import os
import shutil

sortDirFile = open('sortDirs.txt', 'r')
sortDirList = sortDirFile.read().splitlines()
print(sortDirList) #test

tagList = ['A_','B_'] #for loop!

fileDir = 'C:\\Users\\Serban\\Desktop\\%s'
fileList = os.scandir(fileDir %(''))
nameList = [] #this list is read for the file names scanned in os.scandir(fileDir)

for item in fileList: #for every item resulting from os.scandir(fileDir)...
	if item.is_file(): 
		nameList.append(item.name)
	elif item.is_dir() and item.name not in tagList: #if the destination folder is in the source folder and has the same name as its tag, the program will try to move it into itself, throwing up an error.
		nameList.append(item.name)

for sortDir in sortDirList:
	if sortDir == sortDirList[0]:
		for fileName in nameList: #reads every item in the list defined at the top
			if fileName.__contains__(tagList[0]): #tags and directories should be user-definable without having to edit the source code
				shutil.move(fileDir %(fileName), sortDirList[0] %(fileName))
				print(fileName) #testing feature
	elif sortDir == sortDirList[1]:
		for fileName in nameList:
			if fileName.__contains__(tagList[1]): #the program should check filenames for as many tags as there are tags; therefore, it should be able to 'generate' an elif (or something similar) for every tag
				shutil.move(fileDir %(fileName), sortDirList[1] %(fileName))
				print(fileName) #testing feature
    




