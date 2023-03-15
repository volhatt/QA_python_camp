# STRINGS manipulation

# tasks
# 1
"""
make 2 strings
1 - 'xo' repeating 5 times
2 - 'ox' repeating 5 times

1. PRINT concatenate both strings
2. PRINT strings with join and  different
 separators ( space, comma, etc ) between char-s
"""

def task_1():
    str_1 = 'xo' * 5
    str_2 = 'ox' * 5
    strings = '\n' + str_1 + '\n' + str_2
    strings_separated = ' '.join(str_2+str_1)
    print(strings)
    print(strings_separated)
    return "strings are immutable"

print(task_1())

# round number
print(round(2.3))

import math

print(math.ceil(2.3))

print(math.floor(2.3))

print(abs(-19))  # модуль числа / absolute number

"""
	\<newline>
	\'
	\'
	\&
    \t
"""

# strings
"""
returns strings:
lower()
capitalize()
title()
upper()
swapcase()

returns boolean:
endswith()
startswith()
"""