from os import listdir
from os.path import isfile, join, isdir

mypath = './'
onlydirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]

for dir in onlydirs:
    if dir.startswith('.') or dir == 'script':
        continue
    print(f"{dir}:")
    current_path = './' + str(dir) + '/'
    onlyfiles = [f for f in listdir(current_path) if isfile(join(current_path, f))]
    for file in onlyfiles:
        print(file)
