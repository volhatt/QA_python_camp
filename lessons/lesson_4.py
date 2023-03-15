CON = 3.14  # Constant
glob_var = 'test'  # global


def another_function():
    another_variable = 'something'
    return another_variable

def check_var(another_from_outside):
    print(('*'* 10))
    print(CON)
    print(glob_var)
    print(another_from_outside)


def update_var():
    print('*' * 10)
    global CON
    CON = 100
    global glob_var
    glob_var = 'new value'
    print(CON)
    print(glob_var)


# temp = another_function()
# check_var(temp)
# # update_var()
# print(CON)
# print(glob_var)

tests = [(1, 'test'), (2, 'scesial')]
# for el in test:
#     print(el)
print(len(tests))

def test_tuple(tu):
    print(f"Это мой тест с моим кортежем. Элемент 1 - {tu[0]} и элемент 2 - {tu[1]})")

tests.append((3, 'Olga'))

# print(tests)
#
# for test in tests:
#     print(test)
#     for tu in test:
#         print(tu)


# slicing
singers = "Peter, Paula, and Mary"

peter_start = singers.find('P')
peter_end = peter_start + len('peter')
peter = singers[peter_start:peter_end]


sting_start = singers.find('P', 2)
sting = singers[sting_start:sting_start+len('paula')]


mary_start = singers.find('M')
mary = singers[mary_start:mary_start+len('mary')]

print(peter)
print(sting)
print(mary)


st = 'www.blabla.com/html/dfslj'
print(st[4:10])

print(f" a in my string {singers.count('a')}")
print(f" Mary in my string {singers.count('Mary')}")

lst = ['one', 'two', 'three']

# for el in lst:
#     print(el)
#
# for el in range(len(lst)):
#     print(el)
#
# for el in range(len(lst)):
#     print(lst[el])
#
# l = 0
# while l < len(lst):
#     print(lst[l])
#     l += 1

print(lst.index('one'))


# how we can create list
lst = [1, 3, 4, 5]
lst_2 = list('test')
list_3 = list(range(5))
list_4 = []
for i in range(5):
    list_4.append(i)
print(f" list_4 {list_4}")

list_5 = [element for element in range(5, 20)]
print(f" list_5 {list_5}")

d = {'one': 1, 'two': 2, 'three': 3}
list_6 = list(d.keys())
print(f" list_6 {list_6}")
list_7 = list(d.values())
print(f" list_7 {list_7}")

