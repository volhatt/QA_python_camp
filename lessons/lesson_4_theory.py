###
# Classes
# Errors

### Classes

"""
First, just as Python provides a way to define new functions in your programs,
 it also provides a way to define new classes of objects.
we create a new instance with a syntax that looks like a function call
Each instance can have attributes, sometimes called instance variables. These are just like other variables in Python.
We use assignment statements, with an =, to assign values to them.

Classes have associated methods, which are just a special kind of function.
"""

## import modules
"""
Lots of other functions are not built into the core of Python that are readily
 available. They're part of a standard library of modules. A module is a code
  file that defines some functions that can be used by other programs. 
  Before you can invoke a function that's from a standard library module, 
  you need to tell the Python interpreter to you make it available and that's 
  what the import statement does.
"""

## import random module
"""
import random

prob = random.random()
print(prob)

diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)

prob = random.random()
result = prob * 5
print(result)


"""


###### ERRORS - catch , debug, understand

"""
syntax errors
runtime errors
logic errors ( semantic errors ?)

You should be able to 
distinguish between three types of errors; Syntax errors, 
Runtime errors and Semantic errors. 

--> SYntax error - found by compiler:
>>> print('Hello )
SyntaxError: EOL while scanning string literal

print(5 + )

--> Runtime error found by interpreter:
    print(3/0)
ZeroDivisionError: division by zero
examples 
- Misspelled or incorrectly capitalized variable and function names
- Attempts to perform operations (such as math operations) on data of the
 wrong type (ex. attempting to subtract two variables that hold string values)
- Dividing by zero
- Attempts to use a type conversion function such as int on a value that
can’t be converted to an int

--> Semantic errors - found by programmer ( or tester )
when you forget something - code run, but it actually wrong - causes bugs
--> removing bug - we name debugging
--> how to debug in IDLE


"""

#### string slicing  String index


#### join


