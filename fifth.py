"""
DATA STRUCTURES

IMMUTABLE DATA STRUCTURES
TUPLES

MUTABLE DATA STRUCTURES
SETS
LISTS
DICTIONARIES


"""
from traceback import print_tb

# TUPLES () - ordered, immutable, allows duplicate elements
x = (1, 2, 3, 4, 5, 5, 5)
y = ['apple', 'banana', 'cherry']
z = tuple(y)
zz = x + z # concatenation
# print(zz[5]) # indexing
# print(zz[2:5]) # slicing
# print(zz[::-1]) # reversing
# print(len(zz))
# print(zz.count(5)) # count occurrences of an element
# print(zz.index('banana')) # find index of an element



#SETS {} - unordered, mutable, no duplicate elements
xy = {1, 2, 3, 4, 5, 5, 5}
# print(xy)
# yy = set([1, 2, 3, 4, 5, 5])
# print(yy, type(yy))
# print(len(yy))
# xy.add(6) # add element
# print(xy)
# xy.remove(3) # remove element
# print(xy)
# removed_data = xy.pop() # remove and return an arbitrary element
# print(removed_data)
# xy.update({7, 8, 9}) # add multiple elements
# print(xy)
# intersection = xy.intersection(yy) # common elements
# print(intersection)
# union = xy.union(yy)
# print(union) # all elements
#
# difference = xy.difference(yy) # elements in xy but not in yy
# print(difference)


# # LISTS []- ordered, mutable, allows duplicate elements
a = ['apple', 'banana', 'cherry', 'apple', 'banana']
b = list((1, 2, 3, 4, 5))
# print(b, type(b))
# print(a[1]) # indexing
# print(a[1:3]) # slicing
# print(a[::-1]) # reversing
# a.append('apple')
# a.append("1") # adding an element
# a.extend(b)
# print(a)
# a.remove('banana')
# print(a)
# print(len(a))
# print(a.count('banana'))
# print(a.index('cherry'))
# popped = a.pop(a.index('cherry'))
# print(popped)
#
# for i in a:
#     print(f"i love {i}")


# DICTIONARIES {} - unordered, mutable, no duplicate keys
d = {
    "name": "John",
    "_23": 30,
    "city": "New York",
    "name": "Jane"  # duplicate key, will overwrite the previous value
}
e = dict(dad="John", socre=30, home="New York")
d.update(e)
# print(d)
# name = d["name"] # accessing value by key
# d['name'] = 'Del'
# print(d)
# popped_item = d.pop('name')
# print(popped_item)
#
#
# multiples_2 = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         multiples_2.append(i)
# print(multiples_2)
#
# keys = ['name', 'age']
#
# for key, value in d.items():
#     print(f"{key}: {value}")
#     if key in keys:
#         d.pop(key)
#
# print(d)


n = 30
counter = 1

for i in range(1, n + 1):
    nums = []
    for j in range(i):
        if counter > n:
            break
        nums.append(str(counter))
        counter += 1

    print(" ".join(nums))















