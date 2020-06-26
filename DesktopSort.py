import os
import shutil
tag_text = open('sortTags.txt', 'r')
tag_list = tag_text.read().splitlines()
print(tag_list)
to_text = open('sortDirs.txt', 'r')
to_list = to_text.read().splitlines()
print(to_list)
from_text = open('sourceDirs.txt', 'r')
from_list = from_text.read().splitlines()
from_dirscan = []
for directory in from_list:
	for item_entry in os.scandir(directory %('')):
		from_dirscan.append(item_entry)
for item in from_dirscan:
	if item.name.__contains__(tag_list[0]):
		shutil.move(item, to_list[0] %(item.name))
	elif item.name.__contains__(tag_list[1]):
		shutil.move(item, to_list[1] %(item.name))


