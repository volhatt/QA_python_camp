import string

chars = list(string.ascii_lowercase[:10])


# for i in range(11):
#     print(i, chars[i-1])

# for char, num in enumerate(chars, 1):
#     print(char, num)

def print_first_element_of_the_string(s):
    print("\n####### new code ########")
    print(type(s))
    print(type(type(s)))
    if str(type(s)) == "<class 'str'>":
        print(s[0])
        print('Hooray')
    else:
        print("invalid parameter")

    print("\n####### end code ########")


st = 'a lalll a '
num = 5

# print_first_element_of_the_string(st)
# print_first_element_of_the_string(num)

# name = input("Enter your name:")
#
# print(f"My name is {name}")


# age = input("how old are you? ")
#
# print(f"Next year your age {int(age) + 1}")

"""
input - number  -> hours, minutes , seconds 
66
0 hr 1 m 6 s

9
0 hr, 0 minutes 9 sec
"""
# ==
# is
# comarison operator

a = list(range(3))
b = a

# copy

c = list(a)
print("\n####### new code ########")
# formatting string
# 1 %
name = 'Olga'
age = 100
msg = 'My name is %s and my age is %s' % (name, age)
print(msg)

print("\n####### new format ########")
# format
msg = 'My name is {} and my age is {}'
print(msg.format(name, age))

print("\n####### f string  ########")
msg = f'My name is {name} and my age is {age}'
print(msg)

print("\n####### template ########")
from string import Template
t = Template('Hello, $name')

print(t.substitute(name=name))