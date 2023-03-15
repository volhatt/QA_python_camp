"""
1. Boolean operators
2. Dictionary, methods
"""

### 1 Boolean operators
"""
Boolean logic is named after George Boole, who developed a whole system of mathematics based on two values, called true
 and false, and the operations on them—AND, OR, and NOT.
"""

### 2. Dictionary, methods
"""
Method      Parameters  Description
keys        none        Returns a view of the keys in the dictionary
values      none        Returns a view of the values in the dictionary
items       none        Returns a view of the key-value pairs in the dictionary
get         key         Returns the value associated with key; None otherwise
get         key,alt     Returns the value associated with key; alt otherwise
"""
inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():  # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())  # Make a list of all of the keys
print(ks)
print(ks[0])  # Display the first key

for akey in sorted(
        inventory.keys()):  # If you want to visit the keys in alphabetic order, you must use the sorted function to produce a sorted collection of keys
    pass

for k in inventory:
    print("Got key", k)

for v in inventory.values():  # get values
    print("Got", v)

for k, v in inventory.items():  # get items
    print("Got", k, "that maps to", v)
# Safety:
# 1. The first approach is to use the in and not in operators,
# which can test if a key is in the dictionary
if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")
# 2 The second approach is to use the get method
print(inventory.get("apples"))
print(inventory.get("cherries", 0))

# copy and alias dictionary
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
yourdict = mydict
yourdict["elephant"] = 999
print(mydict["elephant"])
mydict["elephant"] = 2
print(yourdict["elephant"])
yourdict is mydict

# Dictionary accumulation pattern ( count characters in the string )
stri = '343 sdf dsfd'
letter_counts = dict()
for c in stri:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] += 1

# replace with:
for c in stri:
    letter_counts[c] = letter_counts.get(c, 0) + 1
