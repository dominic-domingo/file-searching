# Created by Dominic Domingo on Jan 2015 for a project in ICS 32
# Programming w/ Software Libraries.
from pathlib import Path
import shutil

def user_interface() -> None:
    ''' Main UI '''
    while True:
            d = input()
            directory = _dir_search(d)
            
            secondinput = input()
            try:
                secondinputsplit = secondinput.split(maxsplit=1)
                # maxsplit = 1 in case 2nd part of user input contains spaces
                
                if secondinputsplit[0] == 'N':
                    files =_filename_search(directory, secondinputsplit[1])
                elif secondinputsplit[0] == 'E':
                    files = _extension_search(directory, secondinputsplit[1])
                elif secondinputsplit[0] == 'S':
                    files = _size_search(directory, int(secondinputsplit[1]))
                    # turns second part of user input into an int
                else:
                    # if first part of input is not N E or S
                    print('ERROR')
                    user_interface()
            except:
                # if user input cannot be split or if any functions raise
                # an exception, it will go here. The program will start over.
                print('ERROR')
                user_interface()
                
            thirdinput = input()
            try:
                thirdinputsplit = thirdinput.split(maxsplit=1) 
            
                if thirdinputsplit[0] == 'P':
                    for file in files:
                        print(file)
                elif thirdinputsplit[0] == 'F':
                    _print_first_lines(files)
                elif thirdinputsplit[0] == 'D':
                    _duplicate_files(files)
                    for file in files:
                        print(file)
                elif thirdinputsplit[0] == 'T':
                    _touch_files(files)
                    for file in files:
                        print(file)
                else:
                    print('ERROR')
                    user_interface()
            except:
                print('ERROR')
                user_interface()
               

def _dir_search(dir_name: str):
    '''Converts user's input of a string into a Path object'''
    p = Path(dir_name)
    if p.is_dir():
        return p
    else:
        print('ERROR')
        user_interface()

# Second line of input
def _filename_search(path: Path, filename: str) -> [Path]:
    ''' Searches for files in the directory that have the name given and returns
    a list of Paths. '''
    result = []
    for item in path.iterdir():
        if item.is_dir():
            result.extend(_filename_search(item, filename))
        else:
            if item.name == filename:
                result.append(item)
    return result
            
    
def _size_search(path: Path, size: int) -> [Path]:
    ''' Searches for file in directory. '''
    result = []
    for item in path.iterdir():
        if item.is_dir():
            result.extend(_size_search(item, size))
        else:
            if item.stat().st_size > size:
                result.append(item)
            
    return result

def _extension_search(path: Path, extension: str) -> [Path]:
    ''' Searches for all files that have the given extension in directory. '''
    result = []
    for item in path.iterdir():
        if item.is_dir():
            result.extend(_extension_search(item, extension))
        else:
            if extension[0] != '.':
                extension = '.'+extension
            if item.suffix == extension:
                result.append(item)
    return result

# Third line of input
def _print_first_lines(files: list) -> None:
    ''' Prints the first line in each file on the list. '''
    for file in files:
        with file.open() as path:
            print(file)
            print(path.readline())
            path.close()
    
def _duplicate_files(files: list) -> [Path]:
    ''' Duplicates files and gives extension .dup '''
    newfilenames = []
    for i in range(len(files)):
        newfilenames.append(str(files[i])+'.dup')
        shutil.copy(str(files[i]), str(newfilenames[i]))
    return files

def _touch_files(files: list) -> [Path]:
    ''' Changes file's "last modified" time to the current time. '''
    for file in files:
        file.touch(exist_ok=True)
    return files

if __name__ == '__main__':
    user_interface()
    
