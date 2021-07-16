import sys

HASH_INDEX = 1

hash_val = sys.argv[HASH_INDEX]

print(f"handling {hash_val}")

keyspace = None

with open("changed_files.meta", "r") as changed_files:
    lines = [line.rstrip() for line in changed_files]
    for line in lines:
        splits = line.split('/')
        # find first one in non hidden dir
        if len(splits) == 2 and not splits[0].startswith('.'):
        	keyspace = splits[0]
        	break

print(f"keyspace:{keyspace}")


