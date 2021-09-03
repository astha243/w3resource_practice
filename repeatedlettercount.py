import collections

string = "thequickbrownfoxjumpsoverthelazydog"
frequencies = collections.Counter(string)
repeated = {}

for key, value in frequencies.items():

    if value > 1:
        repeated[key] = value


print(repeated)