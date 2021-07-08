from os import listdir
from os.path import isfile, join, isdir
from integer import Integer

mypath = './'
onlydirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]

def is_valid_migration_name(name):
	if len(name) > 64:
		print(f'filename too long: {name}')
		exit(1)

	if not name.endswith('.sql'):
		print(f'{name} not with sql extension: {name}')
		exit(1)

	parts = name.split('_')
	if len(parts)  < 2:
		print(f'{name} not contains _')
		exit(1)

	version = parts[0]
	if len(version) != 4:
		print(f'version {version} not in good length.')
		exit(1)

	if not version.isnumeric():
		print(f'version {version} not numeric')

	return Integer.parseInt(version);  


for dir in onlydirs:
    if dir.startswith('.') or dir == 'script':
        continue
    print(f"{dir}:")
    current_path = './' + str(dir) + '/'
    onlyfiles = [f for f in listdir(current_path) if isfile(join(current_path, f))]
    versions = {}
    for file in onlyfiles:
        print(file)
        next_version = is_valid_migration_name(file)
        if next_version in versions:
        	print(f'find duplicate version in {dir}')
        	exit(1)

        print(next_version)
        versions.add(next_version)


    exit(1)



    
