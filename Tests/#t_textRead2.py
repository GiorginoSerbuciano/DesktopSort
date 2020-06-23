#t_textRead2.py
tagList = []

tagFile = open('tagfile2.txt','r')
tagList.append(tagFile.read().split(','))
print(tagList)
print(tagList[1]) #does not work!

