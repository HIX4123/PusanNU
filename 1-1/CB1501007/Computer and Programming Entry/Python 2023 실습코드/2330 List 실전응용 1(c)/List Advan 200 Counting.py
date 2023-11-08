big_list = ['3', '7', '3', '3', '5', '3', '5', '1', '1', '7', '3', '5', '5',
       '3', '5', '5', '5', '1', '7', '7', '1', '1', '7', '7', '3', '7',
       '3', '5', '1', '5', '5', '3', '3', '5', '1', '1', '1', '1', '7',
       '3', '7', '1', '5', '1', '7', '3', '5', '5', '6', '5', '7', '1',
       '5', '1', '5', '1', '3', '7', '7', '5', '3', '1', '1', '5', '5',
       '5', '1', '5', '1', '7', '3', '7', '1', '7', '5', '7', '1', '5',
       '3', '5', '3', '5', '3', '5', '5', '1', '3', '5', '3', '7', '1',
       '5', '7', '3', '1', '7', '5', '7', '7', '1']


counts = {}
for num in big_list:
    if num not in counts:
        counts[num] = 0
    counts[num] += 1
print(counts)

import collections
# defaultdict is a data type which behaves like a dictionary, but automatically initialises any key that doesn't exist. We have to specify what the types of the values should be. For instance:

# A defaultdict with values of type int
counts = collections.defaultdict(int)

print(f" counts['new_key'] = { counts['new_key']} ")
print(f" counts['5'] = { counts['5']} ")