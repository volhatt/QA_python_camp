# aliases  vs clone

a = [81,82,83]
b = [81,82,83]

print(a is b)
​
b = a
print(a == b)
print(a is b)


b[0] = 5
print(a)

# clone
c = a[:]
#When an object is concatenated with another using +=, it extends the 
#original object. If this is done in the longer form (item = item + object)
# then it makes a copy.

'''
False
True
True
[5, 82, 83]
'''