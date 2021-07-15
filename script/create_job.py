import sys

HASH_INDEX = 1

hash_val = sys.argv[HASH_INDEX]

print(f"handling {hash_value}")

with open("changed_files.meta", "r") as changed_files:
	lines = [line.rstrip() for line in changed_files]
    	for line in lines: 
    		print(line)


