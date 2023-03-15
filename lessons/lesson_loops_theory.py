# 1. Loops
# 2. While

"""
There is another Python statement that can also be used to build an iteration.
 It is called the while statement. The while statement provides a much more
general mechanism for iterating. Similar to the if statement,
it uses a boolean expression to control the flow of execution.
 The body of while will be repeated as long as the controlling boolean
  expression evaluates to True.

We can use the while loop to create any type of iteration we wish,
including anything that we have previously done with a for loop.
For example, the program in the previous section could be rewritten using
while. Instead of relying on the range function to produce the numbers for our
summation, we will need to produce them ourselves.

remember about accumulator variable
counter - where we are, track where we are
"""
def sum_to(aBound):
    """ Return the sum of 1+2+3 ... n """
    the_sum = 0
    a_number = 1
    while a_number <= aBound:
        the_sum = the_sum + a_number
        a_number = a_number + 1
    return the_sum
print(sum_to(4))

print(sum_to(1000))
"""
One of type of while loop - One very common pattern is called a listener loop. 
Inside the while loop there is a function call to get user input. The loop 
repeats indefinitely, until a particular input is received.
"""
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)

"""
homework - find possible error, add validating the input
"""
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()