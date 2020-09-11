DESKTOPSORT v2.0 // 11.09.2020 // By using DESKTOPSORT, you assume the responsibility for any loss of information. 

1.1 INTRODUCTION
DESKTOPSORT is a lightweight file sorting program built in Python 3.8.2. 
It relies on recognizing user-determined tags at the beginning of file names.
While it requires no Python experience to run, it helps to be familiar with the language for troubleshooting.
Visit https://github.com/GiorginoSerbuciano/DesktopSort for version history.

1.2 SETUP
First-time users will be automatically prompted with a wizard guiding them through the setup.
To get started, run DesktopSort.py. 
You can run this wizard at any time by executing setup.py.

1.3 MAIN FUNCTIONALITY
DESKTOPSORT is intended as a 'lite' file sorter which works in 4 main steps:
1. Scans the source directories given in sourceDirs.txt, building a list of files in these directories.
2. Reads the names of every file in the list, checking for the tags given in sortTags.txt, building a list of these.
3. Prints the list of all tagged files found and asks for confirmation (see 'noCheck' below).
4. Moves the tagged files to their respective directories given in sortDirs.txt.

1.3.1 noCheck mode
noCheck is a protocol which allows DESKTOPSORT to operate without interfacing with the user.
This means that users will not be prompted with a list of tagged items and a confirmation before moving when noCheck is on.
This could be considered an 'automatic', faster mode of operation.
noCheck is enabled when noCheck.txt is present in the program directory.
To enable it, the user may create a new text file called 'noCheck.txt', or remove the '!' from the pre-existing one.
To disable it, simply delete or change the name of 'noCheck.txt'.

1.4 LIMITATIONS
While it has the capacity to handle volumes of files as great as any other program, it lacks the features of more 'serious' software.

1.4.1 Recommendations
* Operating systems usually disallow '< > : " / \ | ? *' as filename characters. Therefore, avoid using these in your tags. Please note that tags are case-sensitive.
* Using common combinations of letters and symbols as tags (e.g. "do") may result in unwanted displacements of files (e.g. "door.txt").
* Preferably separate tag and name by a symbol (e.g. "A_")!

1.4.2 Long-term limitations
* Can only read sortDirs.txt and sortTags.txt from top to bottom and line-by-line. 
In other words, it reads the sorting directories and tags in the same, corresponding order. 
For the user, this means that if tag "A_" is on the first line of sortTags.txt, then the directory corresponding to tag "A_" must be on the first line of sortDirs.txt. 
Futhermore, there must be one tag per sorting directory (Source directories do not have this limitation!)
DESKTOPSORT has no fancy failsafe against accidentally swapping the order of tags and directories.
These are limitations inherent to the way the program is designed and may be fixed in major versions.

1.4.3 Short-term limitations
* Cannot tell a regular file apart from a vital system file, nor can it distinguish between a file and a directory. Point it only at non-crucial directories and tag only non-crucial files.
* No failsafe against overwriting files with the same name and of any type. 
These limitations will be overcome in subsequent minor versions.

1.5 KNOWN BUGS:
None as of v2.0 (11.09.2020)

1.6 PRIVACY NOTE
DESKTOPSORT does not send or store information about your computer or any files processed by the program during its operation.

~DESKTOPSORT 2020 DEVELOPED FOR EDUCATIONAL PURPOSES AT HAMBURG MEDIA SCHOOL BY GORGA ȘERBAN-AURELIAN~