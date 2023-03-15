# """
# Immutable vs mutable
# new sequense vs changed sequence
# new object or new alias of the same object
#
#
# Note
#
# WP: Don’t Mix Typles!
#
# You’ll likely see us do this in the textbook
#  to give you odd combinations, but when you create lists
#   you should generally not mix types together.
#    A list of just strings or just integers or
#     just floats is generally easier to deal with.
#
# Tuples - just like list but immutable
# how to create
#
#
not_tuple = (30)
my_typle = (30,)

# Tuple as return in function ( if 2 item in return - it is a tuple )
# Tuple unpacking - 2 variable = function that returns 2 values as a tuple example:
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

circumference, area = circleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)

# Tuple assignment with unpacking
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia

# TUPLE = swapping values between variables:
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b, temp)
# with tuple we don't need temp' \
(a, b) = (b, a)

# The pythonic way to consume the results of enumerate, however, is to unpack
# the tuples while iterating through them, so that the code is easier to understand.
# pythonic way to enumerate sequence
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

# with enumerate
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# the .items() dictionary method produces a sequence of tuples.
# unpacking tuple in a multiple variables as a parameter
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked



# Index operation - get specific element of the sequence
#
# why we use typle - какие то данные которые нам нужны так как они есть
# ( данные для тестов)
# разница - мы можем добавлять, менять, апдейтить.
# тупл - не можем.
#
# """
# # квадратные скобки - для лист и для индексинг  []
#
#
# # проход по массиву - ошибка  - часто с while
# или for i in len(list)
# lastch = fruit[len(fruit)-1] !- correct
#
# IndexError: string index out of range on line 3
#
# # slicing
# """
# singers = "Peter, Paul, and Mary"
# print(singers[0:5])
# print(singers[7:11])
# print(singers[17:21])
# Peter
# Paul
# Mary
#
# peter_start = singers.find('P')
#
# peter = singers[peter_start:peter_start + 5]
#
#
# singer_updated = singers[peter_start + 5:]
#
# paul_start = singer_updated.find('P')
# paul  = singer_updated[paul_start:paul_start + 4]
#
# mary_start = singer_updated[paul_start + 4:].find('M')
# mary = singer_updated[paul_start + 4:][mary_start:mary_start+4]
#
#
# print(peter)
# print(paul)
# print(mary)
#
# """
#
# ##### rsplit()
# """
# This tutorials is for How to remove part of string before the last forward slash. you can easily split your url between filename part and the rest. The rsplit() method return splits string from the right at the specified separator and returns a list of strings.
#
# Example-1
# url = 'https://devnote.in/index.html'
# final_url = url.rsplit('/', 1)
#
# print (final_url)
# Output : ['https://devnote.in', 'index.html']
#
# print (final_url[-1])
# Output : index.html
#
# """
#
# ### - IMPORTANT for function and loop
# """
# PASS
# CONTINUE
# RETURN
#
# """
#
# # all ways to create list
# lst  = ([0] * 4)
# lst = list('test')
# lst = list(range(4))
# lst = []
# lst = [x for x in 'test']
# d = {'one': 1, 'two': 2, 'three': 3}
# lst = list(d.keys())
#
# = ==
# concatenate list
# alist = [1,3,5]
# blist = [2,4,6]
# print(alist + blist)
#
# alist = [1,3,5]
# print(alist * 3)
# [1, 3, 5, 1, 3, 5, 1, 3, 5]
#
# ####  count with list and string , index
# l = [1, 3, 5, 1, 3, 5, 1, 3, 5]
# l.count(1)
# 3
#
#
# >>> l.index(1)
# 0
#
# a = "I have had an apple on my desk before!"
# print(a.count("e"))
# print(a.count("ha"))
#
# = = = = index
# music = "Pull out your music and dancing can begin"
# bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]
#
# print(music.index("m"))
# print(music.index("your"))
#
# print(bio.index("Metatarsal"))
# print(bio.index([]))
# print(bio.index(43))
#
#
# ERROR
# seasons = ["winter", "spring", "summer", "fall"]
# print(seasons.index("autumn"))  #Error!
# ValueError: list.index(x): x not in list on line 3
#
#
# qu = "wow, welcome week! Were you wanting to go?"
# ty = qu.count("we")
#
#
# # There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
