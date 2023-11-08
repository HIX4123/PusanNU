
import random

items = ['here', 'are', 'some', 'strings', 'of',
         'which', 'we', 'will', 'select', 'one']

rand_item = items[random.randrange(len(items))]

print("rand_item= ", rand_item)


rand_items = [items[random.randrange(len(items))]
              for item in range(4)]



print("rand_items = ", rand_items)