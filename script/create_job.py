import sys

HASH_INDEX = 1

hash_val = sys.argv[HASH_INDEX]

print("handling": hash_val)

with open("changed_files.meta", "r") as changed_files:
	lines = [line.rstrip() for line in changed_files]
    	for line in lines: 
    		print(line)


