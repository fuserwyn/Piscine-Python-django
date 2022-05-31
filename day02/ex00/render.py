import sys
import os
import re
import settings

def main():
    if (len(sys.argv) != 2):
        return print ("wrong number of arguments, use one arg") 
    if os.path.isfile(sys.argv[1]) == False:
        return print("non-existing file")
    pattern = '.template'
    result = re.search(pattern, sys.argv[1])
    if result == None:
         return print("use extension: .template")
    f = open(sys.argv[1], "r")
    string = "".join(f.readlines())
    file = string.format(name=settings.name,
                            surname=settings.surname,
                            title=settings.title,
                            music=settings.music,
                            python=settings.python, 
                            git=settings.git,
                            cpp=settings.cpp)
    f = open("myCV.html", "w")
    f.write(file)
    f.close()
    
if __name__ == '__main__':
    main()
