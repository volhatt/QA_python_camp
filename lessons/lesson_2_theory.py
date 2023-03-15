####    Lesson 2

# btw - about light editors 

# 1. how to find help in Python
# 2. Python naming conventions 
# 3. Miscellaneous about what already said
# 4. Strings more about that 
# 5. Splitting, Concatenating, and Joining Strings in Python
# 6. Built-in functions 
# 7. Operator IN and NOT IN  strings
# 8. Built-in function for strings
# 9. String Indexing

# STRING INDEXING and SLICING  ???


##############  # 1. how to find help in Python
"""
parameter - object: (Optional) The object whose documentation needs to be printed on the console.
Returns a help page.
help(list)
help(str)
help(print)
import math
help(math)
"""

############## 2. Python naming conventions
"""
    https://www.python.org/dev/peps/pep-0008/
    https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
    
"""

#################### # 3. Miscelanious about what already said about number

"""
	about float - we can just add . to the int
	we can cast
	
	>>>  a = 2 * 3
	>>> a
	6
	>>> b = 2. * 3
	>>> b
	6.0
	>>> type(a)
	<class 'int'>
	>>> type(b)
	<class 'float'>

	
	>>> 1.79e308
	1.79e+308
	>>> 1.8e308
	inf
	
	complex number - class comlex : 
	type(2 + 3j)
	<class 'complex'>
"""

######### 4. More about Strings in Python
"""
	More about escaping in the string  - escape - backslash \
	>>> print('This string contains a single quote (') character.')
	SyntaxError: invalid syntax
	
	>>> print('This string contains a single quote (\') character.')
	This string contains a single quote (') character.
	
	\<newline>
	\'
	\'
	\&
	
	>>> print('a\
	... b\
	... c')
	abc
	
	>>> print('foo\tbar')
	foo     bar
	
	https://www.python-ds.com/python-3-escape-sequences
"""

######### 5. Splitting, Concatenating, and Joining Strings in Python
"""
    split()
    w/out separator

    how to use

    string.split()
    'a,b,c'.split(',')
    s = 'ola, vasya, petya'
    s.split()
    s.split(',')

    s1 = 'ola vasya petya'
    s.split()
    s.split(' ')

    s2 = 'ola  vasya  petya'
    s.split(' ')

    ######## limiting wiht MAXSPLIT
    >>> s = "this is my string"
    >>> s.split(maxsplit=1)
    ['this', 'is my string']

    What happens when you give a negative number as the maxsplit parameter?
    .split() will split your string on all available separators, which is also the default behavior when maxsplit isn’t set.
    (advanced with list involved https://realpython.com/python-string-split-concatenate-join/#splitting-strings -> "Section Comprehension Check" )

    ############ Concatenating With the + Operator
    remember string are immutable
    >>> orig_string = 'Hello'
    >>> orig_string + ', world'
    'Hello, world'
    >>> orig_string
    'Hello'
    >>> full_sentence = orig_string + ', world'
    >>> full_sentence
    'Hello, world'

    ############ Going From a List to a String in Python With .join()
    >>> strings = ['ola', 'vova', 'misha']
    >>> ','.join(strings)
    'ola,vova,misha'
    How could you make the output text more readable?
    >>> strings = ['ola', 'vova', 'misha']
    >>> ', '.join(strings)
    'ola,vova,misha'
"""

######### 6. Built-in functions 
"""
	https://docs.python.org/3.10/library/functions.html
	
"""

#################### # 7. Operator IN and NOT IN  strings
"""
	The in & not in Operators
	>>> s = 'foo'
	>>> s in 'That\'s food for thought.'
	True
	>>> s in 'That\'s good for now.'
	False
	
	>>> 'z' not in 'abc'
	True
"""

#################### # 8. Built-in function for strings
"""
Strings are one of the data types Python considers immutable,
 meaning not able to be changed.
In fact, all the data types you have seen so far are immutable.
	build in functions in STRING
	chr()	Converts an integer to a character ASCII
	ord()	Converts a character to an integer ASCII
	len()	Returns the length of a string
	str()	Returns a string representation of an object
	
	>>> ord('€')
	8364
	>>> ord('∑')
	8721
	>>> ord('a')
	97
	>>> ord('#')
	35
	
	>>> s = 'I am a string.'
	>>> len(s)
	14
	
	>>> s = 'foobar'
	>>> s = s.replace('b', 'x')
	>>> s
	'fooxar'
	
	
	CASE CONVERSION
	s.capitalize() returns a copy of s with the first character 
	converted to uppercase and all other characters
	 converted to lowercase:
	>>> s = 'foO BaR BAZ quX'
	>>> s.capitalize()
	'Foo bar baz qux'
	
	s.lower() Converts alphabetic characters to lowercase.
	>>> 'FOO Bar 123 baz qUX'.lower()
	'foo bar 123 baz qux'
	
	s.swapcase() Swaps case of alphabetic characters.
	>>> 'FOO Bar 123 baz qUX'.swapcase()
	'foo bAR 123 BAZ Qux'
	
	s.title()  Converts the target string to “title case.”
	>>> 'the sun also rises'.title()
	'The Sun Also Rises'
	
	s.upper() Converts alphabetic characters to uppercase.
	>>> 'FOO Bar 123 baz qUX'.upper()
	'FOO BAR 123 BAZ QUX'
	
"""

#################### # 9. String Indexing
