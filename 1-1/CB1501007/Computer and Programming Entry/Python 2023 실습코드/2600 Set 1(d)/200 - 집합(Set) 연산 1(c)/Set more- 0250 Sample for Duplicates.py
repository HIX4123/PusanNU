

from random import choice, sample
choice(list(set([1, 2, 3])))

# random.sample(), selecting 1 random element
print(sample(set([1, 2, 3, 6, 7, 8, 9,10]), 4))

a = sample(set([1, 2, 3]), 1)
print(a, a[0])

my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
my_set = set(my_list)
my_list = list(my_set) # No duplicates
print(my_list)

my_elem = choice(my_list)
print(my_elem)

another_elem = choice(list(set([1, 1, 1])))
print(another_elem)

