# file-searching
Basic file searching program in Python. Used to understand recursive functions and when to use recursion.
Program was written with the assumption that user knows how to input commands into the program.

First line of input should be the directory to be searched for. (eg: C:\Program Files\Adobe or /Users/Dom/Documents)


Second line of input can take three options: N E or S.

N followed by a name searches for files by that name. (eg: N readme.txt)

S followed by a number searches for files greater than that size (eg: S 200000)

E followed by an extension searches for files with that extension (eg: E py or E .py)


Third line of input can take four actions on the file: P F D T

P will print the names of all the files found.

F will print the first line of all files. (If file is not text, will raise error.)

D will duplicate the file in the same folder and add the extension .dup

T will touch the file and  change the file's "last modified" date to the current file

