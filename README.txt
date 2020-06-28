DESKTOPSORT v1.0 // 28.06.2020 // USE THIS PROGRAM WITH CARE!

INSTRUCTIONS:
1. Place the program and accompanying text files together anywhere on your computer.
2. In sortTags.txt, write the tags you want the program to look for, one on each line
3. In sourceDirs.txt, write the directories you want the program to look for tagged files in, one on each line.
4. In sortDirs.txt, write the directories you want the program to send your tagged files to, one on each line.
5. Tag files by adding your tag of choice to the names of files you wish to sort.
6. If there are tagged files within the source directories, running the program will move them to the sorting directories.

CAUTIONS:
* Choose tags which are not common combinations of letters and symbols. If you use e.g. "do" as a tag, any items whose names contain it, such as "door.txt" or "Windows" will be moved by accident. Tags such as "1_" or "AB!" should not cause this program.
* USE THIS PROGRAM WITH CARE, pointing it only at directories where you are sure no important files will be lost, as it has no failsafe for displacing system files, nor for overwriting files. 
* Tags are case sensitive.

LIMITATIONS as of v1.0:
* Number of tags and sorting directories is currently limited to TWO. This limitation does not apply to source directories, although it is not known what the performance impact of working with many of them would be.
* The program must be run every time the user wishes to sort their files.
* There is no GUI.

NOTES ON PROGRAM VARIABLES:
tag_text: Textfile containing tags
tag_list: List containing tags from tag_text
DESTINATION DIRECTORIES:
to_text: Textfile containing destination directories.
to_list: List containing dest. dirs. from to_text.
SOURCE DIRECTORIES:
from_text: Textfile containing source directories.
from_list: List containing source directories from from_list.
from_dirscan: List containing the names of all files scanned in the source directories.
