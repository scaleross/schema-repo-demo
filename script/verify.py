from os import listdir
from os.path import isfile, join, isdir

mypath = './'
onlydirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]

for dir in onlydirs:
    print(dir)
