# empty_list = []
# empty_list = list()
# none_list = [None] * 10
# collections = ['list', 'tuple', 'dict', 'set']
# user_data = [
# ['Elena', 4.4],
# ['Andrey', 4.2]
# ]
# print(none_list)
# print(collections)
# print(user_data)
#
# print( 'Try watch size')
# print(len(collections))
# print(dir(collections))
# print(collections.__len__())  # эквивалентно len(collections), но куда изящнее
#
# print( 'Try index calls')
# print(collections)
# print(collections[0])
# print(collections[-1])
#
# collections[3] = 'frozenset'
#
# print( 'Try watch size')
# print('tuple' in collections )

# range_list = list(range(10))
# print(range_list)
# print(range_list[1:3])
# range_list[::2]
# range_list[::-1]
# range_list[5:1:-1]
# lis = [1,2,3,4,5]
# print(lis[::-1])
# print(lis[::-2])
#
# print(range_list[:] is range_list)


# collections = ['list', 'tuple', 'dict', 'set']
# for collection in collections:
#     print('Learning {0}...'.format(collection))
#
#
# for idx, collection in enumerate(collections):
#     print('#{0} {1}'.format(idx, collection))
#
# collections.append('OrderedDict')
# print(collections)
#
# collections.extend(['ponyset', 'unicorndict'])
# print(collections)
#
# collections += [None]
# print(collections)
#
# del collections[4]
# print(collections)
# numbers = [4, 17, 19, 9, 2, 6, 10, 13]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
#
#
# tag_list = ['python', 'course', 'coursera']
# print(', '.join(tag_list))
#
#
# import random
# numbers = []
# for _ in range(10):
#     numbers.append(random.randint(1, 20))
# print(numbers)
#
# print('sorted')
#
# print(sorted(numbers))
#
# numbers.sort()
# print(numbers)
#
# print(sorted(numbers, reverse=True))
# numbers.sort(reverse=True)
# print(numbers)

#
# print(sorted(numbers, reverse=True))
# numbers.sort(reverse=True)
# print(numbers)
#
# empty_tuple = ()
# empty_tuple = tuple()
#
# immutables = (int, str, tuple)
#
# blink = ([], [])
# blink[0].append(0)
# print(blink)
# print(hash(tuple()))
#
# one_element_tuple = (1,)
# guess_wha  t = (1)
# print(type(guess_what))
# print(type(one_element_tuple))

import random
numbers = []
numbers_size = random.randint(10, 15)
for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))
print(numbers)

numbers.sort()

half_size = len(numbers) // 2
median = None
if numbers_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1:half_size + 1]) / 2
print(median)

import statistics
statistics.median(numbers)
