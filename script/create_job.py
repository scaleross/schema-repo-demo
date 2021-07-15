import sys

HASH_INDEX = 1

hash_val = sys.argv[HASH_INDEX]

print(f"handling {hash_val}")

keyspace = ""
with open("changed_files.meta", "r") as changed_files:
    lines = [line.rstrip() for line in changed_files]
    for line in lines:
        splits = line.split('/')
        if splits == 2:
        	keyspace = splits[0]
        	break


print(keyspace)


