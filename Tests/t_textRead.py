#t_textRead
tags = []

tagFile = open('Tests/tagfile.txt','r')
for line in tagFile:
    tagList = tagFile.readlines()
    print(tagList)
    for line in tagList:
        tags = line[:-1]
        print(tags)




