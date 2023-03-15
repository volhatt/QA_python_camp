# 1. questions from previous lesson and misc
# 2. Input
# 3. In Range function
# 4. Comparison operators == vs is
# 5. String formatting - a little bit of history ( string template )

# 7. Codewar tasks

### questions from previous lesson

# 1 about check if string ( char ? )
# we can check with type()
arg = 'c'
arg_type = type(arg)
if str(arg_type) == "<class 'str'>":
    print("Hooray")
else:
    print("Ha ha ha! good try")
# type of type? -> str(type(arg)), refactor and fix errors.


### about assigning wariables When reading or writing code,
# say to yourself “n is assigned 17” or “n gets the value 17”
# or “n is a reference to the object 17” or “n refers to the
# object 17”. Don’t say “n equals 17”.

### Variable names can never contain spaces.
### +, = etc -

### operator - how update variable
x = 3
# update
x += 1

### Statements and Expressions
"""
statement x = 4+3
but 4+3 - expression
simple literal expression - 35 ( value of 35 is 35 )
value of len('ter') expression is 3
x = len('ter') - it is Statement

In a program, anywhere that a literal value (a string or a number) is acceptable, a more complicated expression is also acceptable. Here are all the kinds of expressions we’ve seen so far:

literal
e.g., “Hello” or 3.14

variable name
e.g., x or len

operator expression
<expression> operator-name <expression>

function call expressions
<expression>(<expressions separated by commas>)

Notice that operator expressions (like + and *) have sub-expressions
 before and after the operator. Each of these can themselves be simple
  or complex expressions. In that way, you can build up to having pretty
   complicated expressions.
"""

### INPUT
"""
input - standart input ( keyboard )
name = input("please enter your name")
print(f"Hello, {name}!")
!!! - always string !, so we need to convert !
age = int(input("how old are you?"))
next_year_age = age + 1
( btw stip())

TASK - convert seconds from INPUT -> to hours, minutes, seconds
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

in real life we add all checks for numbers
"""

#### generators vs iterators in  python
"""
A python generator function lends us a sequence of values to python iterate on. 
Функция генератора Python предоставляет нам последовательность значений для итерации

eg of generator:
>>> def even(x):
       while(x!=0):
           if x%2==0:
                 yield x
              x-=1
>>> for i in even(8):
               print(i)


A Python iterator returns us an iterator object- one value at a time.

"""
##### Len and range 
"""
>>> len(range(1, 20, 2))
10
fundamental buil-in function
The range() function returns a sequence of numbers, starting from 0
by default, and increments by 1 (by default), and stops before a specified number.

The python range() function creates a collection of numbers
 on the fly, like 0, 1, 2, 3, 4.
This is very useful, since the numbers can be used to index
 into collections such as string. The range() function can be
  called in a few different ways.
  
производит генерирует поток данных ( чисел ). 



наиболее частое употребление - looping - run code many times without 
rewrite it again

3 different implementation: customize output : returns a series of n numbers

range(stop)
range(start, stop)
range(start, stop, step)

range(0, 3)
list(range(3))
[0, 1, 2]

What is range(0)? Well range(n) returns n numbers, so this case returns no numbers at all - like the empty list.

>>> list(range(2))
[0, 1]
>>> list(range(1))
[0]
>>> list(range(0))   # n <= 0, no numbers
[]
>>> list(range(-42))
[]

https://realpython.com/python-range/
== == == ==

>>> s = 'Python'
>>> len(s)
6
>>> for i in range(len(s)):
...   print(i, s[i])
... 
0 P
1 y
2 t
3 h
4 o
5 n



"""

## Comparison  == vs is
"""
There’s a difference in meaning between equal and identical
The == operator compares by checking for equality

The is operator, however, compares identities
>>> a = [1, 2, 3]
>>> b = a

>>> a
[1, 2, 3]
>>> b
[1, 2, 3]

>>> a == b
True
>>> a is b
True


make a COPY ! - new concept
>>> c = list(a) 

>>> c
[1, 2, 3]
>>> a == c
True
>>> a is c
False
BOOM
An is expression evaluates to True if two variables point to the same
 (identical) object.

An == expression evaluates to True if the objects referred to by
 the variables are equal (have the same contents).
"""

## String formatting
"""
#1 “Old Style” String Formatting (% Operator)
>>> name = 'Olga'
>>> age = 25
>>> 'Hello, %s' % name
"Hello, Olga"

'Hello, My name is %s and I am %s' % (name, age) 
'Hello, My name is Olga and I am 25'
'Hello, My name is %s and I am %x' % (name, age) 
'Hello, My name is Olga and I am 19'
'Hello, My name is %s and I am %i' % (name, age)
'Hello, My name is Olga and I am 25'
'Hello, My name is %s and I am %d' % (name, age)
'Hello, My name is Olga and I am 25'


#2 “New Style” String Formatting (str.format)
s = 'Hello, My name is {} and I am {}'
s.format(name, age)
'Hello, My name is Olga and I am 25'

'Hello, My name is {name} and I am {age}'.format(name=name, age=age)
'Hello, My name is Olga and I am 25'

#3 String Interpolation / f-Strings (Python 3.6+)
f-string

#4 Template Strings (Standard Library)
from string import Template
t = Template('Hey, $name!')
t.substitute(name=name)
'Hey, Olga!'

"""



