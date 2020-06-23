#t_textRead2.py
tagList = {}

tagFile = open('Tests/tagfile2.txt','r')

tagList.append(tagFile.read().split(','))

print(tagList)


