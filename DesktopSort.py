import os
import shutil
tag_text = open('sortTags.txt', 'r')
tag_list = tag_text.read().splitlines()

to_text = open('sortDirs.txt', 'r')
to_list = to_text.read().splitlines()

from_text = open('sourceDirs.txt', 'r')
from_list = from_text.read().splitlines()
from_dirscan = []

for directory in from_list:
	for item_entry in os.scandir(directory %('')):
		from_dirscan.append(item_entry)

i = 0
move_list=[]
for tag in tag_list:
	for item in from_dirscan:
		if item.name.startswith(tag_list[i]) or item.name.endswith(tag_list[i]):
			move_list.append(item)
	i += 1

i = 0
print(len(move_list), "tagged items have been found.")
if input("Would you like to review a list of these? y/n:   ") == 'y':
	for item in move_list:
		print(item.name)
	if input("Is this list correct? Confirm to move, y/n:   ") == 'y':
		for tag in tag_list:
			for item in from_dirscan:
				if item.name.startswith(tag_list[i]) or item.name.endswith(tag_list[i]):
					shutil.move(item, to_list[i] %(item.name))
					print(item.name, "has been moved to", to_list[i])
			i += 1
else:
	if input("Confirm to move, y/n:    ") == 'y':
		for tag in tag_list:
			for item in from_dirscan:
				if item.name.startswith(tag_list[i]) or item.name.endswith(tag_list[i]):
					shutil.move(item, to_list[i] %(item.name))
					print(item.name, "has been moved to", to_list[i])
			i += 1
	




#hello plis this is tecnikil snitzil and i will do many tecnikil thingses yes yes like delete the internets and also many other thingses like install the program of making beautifuls with computers