for directory in from_list:
	if directory.is_dir() and directory.name not in tag_list:
		from_dirscan.append(os.scandir(directory %(''))
for item in from_dirscan:
	item_name = str(item)
	if item_name.__contains__(tag_list[0]):
		print('Tag 1!')
	elif item_name.__contains__(tag_list[1]):
		print('Tag 2!')
	else:
