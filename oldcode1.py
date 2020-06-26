for sortDir in to_list:
	if sortDir == to_list[0]:
		for fileName in list_of_files: #reads every item in the list defined at the top
			if fileName.__contains__(tag_list[0]): #tags and directories should be user-definable without having to edit the source code
				shutil.move(from_list[0] %(fileName), to_list[0] %(fileName))
				print(fileName) #testing feature
	elif sortDir == to_list[1]:
		for fileName in list_of_files:
			if fileName.__contains__(tag_list[1]): #the program should check filenames for as many tags as there are tags; therefore, it should be able to 'generate' an elif (or something similar) for every tag
				shutil.move(from_list[1] %(fileName), to_list[1] %(fileName))
				print(fileName) #testing feature