import os

print('DESKTOPSORT v1.0 - 28.06.2020\nDESKTOPSORT v2.0 - 04.09.2020')   

print('DESKTOPSORT is an automatic file sorting program built in Python 3.8.2.\n'
'It relies on recognizing user-determined tags at the beginning of file names.\n'
'For more information, visit https://github.com/GiorginoSerbuciano/DesktopSort (Clickable URL in README.txt)\n')

print('DESKTOPSORT 2020 DEVELOPED FOR EDUCATIONAL PURPOSES AT HAMBURG MEDIA SCHOOL\n')

input('Press ENTER to begin the tutorial, or close this window to abandon the program... (You can read the instructions at any time in README.txt.)\n')

input('To get started, place the DESKTOPSORT folder anywhere on your computer.\n' 
'Given that you are reading this, you have most likely done this already. Good work! :)\n'
'Press ENTER to continue...\n')

input('First, we have to point DESKTOPSORT to the directory/ies it should scan.\n' 
'(No worries -- DS only runs locally, so none of your information is sent anywhere.)\n'
'We can do this by entering the desired addresses in sourceDirs.txt, one per line.\n'
'I recommend using this format: C:\\User\\Documents\\Desktop.\n'
'You can have as many of these as you want.\n'
'[!]\n'
'DESKTOPSORT cannot tell a regular file apart from a vital system file, nor can it distinguish between a file and a directory.\n'
'Point at it crucial directories at your risk!\n'
'Press ENTER to continue to your text editor. When done, save and close the file, then return to this screen...\n')
os.startfile('sourceDirs.txt')
input('Now, indicate to DESKTOPSORT where it should send your files.\n'
'Do this by typing in the addresses into sortDirs.txt, just like you did earlier.\n'
'Press ENTER to continue to your text editor. When done, save and close the file, then return to this screen...\n')
os.startfile('sortDirs.txt')
input('Lastly, DESKTOPSORT needs to know what tags to look for.\n'
'Type these in sortTags.txt, one per line.\n'
'Good tags are uncommon combinations of letters, separated by a symbol (e.g. Vp_, Ojh!)\n'
'Make sure that your tags do not contain any symbols that your file system does not allow as names (e.g. \ or /)\n'
'[!]\n'
'Because DESKTOPSORT is not very smart (yet), it needs to read the sorting directories and tags in the same order.\n'
'For example, if you have tag "A_" on the first line of sortTags.txt, then the directory where you want files tagged "A_" to go to should be on line 1 of sortDirs.txt\n'
'Furthermore, it can only handle one tag per directory; not more, not less!\n'
'Press ENTER to continue to your text editor. When done, save and close the file, then return to this screen...\n')
os.startfile('sortTags.txt')
input('Congratulations! If everything went well, DESKTOPSORT should now be ready to operate!\n'
'To sort items on your computer, add your tags to the names of files according to your needs.\n'
'Opening DESKTOPSORT.py will run the script which moves files to their right places.\n'
'Next time you run it, you will not be met with this tutorial any more.\n\n'
'Thanks for using DESKTOPSORT! Hope it serves you well. I would be very glad to hear from you on GitHub!\n'
'~GiorginoSerbuciano\n'
'Press ENTER to end the tutorial...')

