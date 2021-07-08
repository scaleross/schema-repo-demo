from os import listdir
import os
from os.path import isfile, join, isdir

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

	return int(version);  


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

        versions[next_version] = file

    total_versions = len(versions)
    for i in range(1, total_versions + 1):
    	if i not in versions:
    		print(f'version {i} is missing!')
    		exit(1)

    hidden_dir = current_path + '.meta' + '/'
    if not os.path.exists(hidden_dir):
        os.makedirs(hidden_dir)

    migrations_filename = hidden_dir + 'migrations'

    line_count = 1

    with open(migrations_filename, "r") as migration_file:
    	lines = [line.rstrip() for line in migration_file]
    	for line in lines:
    		version, filename = line.split(':')
    		version = int(version)

    		if version != line_count:
    			print('not right sequnce!')
    			exit(1)

    		if version not in versions:
    			print(f'missing version for {migrations_filename}')
    			exit(1)

    		if version in versions and versions[version] != filename:
    			print(f'{version}s filename not match, expect {filename} found {versions[version]}')
    			exit(1)

    		line_count += 1


    with open(migrations_filename, "a") as migration_file:
    	while line_count <= len(versions):
    		migration_file.write(f"{line_count}:{versions[line_count]}\n")
    		print(f"{line_count}:{versions[line_count]}\n")
    		line_count += 1





    
