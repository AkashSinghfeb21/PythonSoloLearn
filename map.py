# The built-in functions map and 
# filter are very useful higher-order
# functions that operate on lists (or similar objects called iterables). 

# The function map takes a function
# and an iterable as arguments, and 
# returns a new iterable with the function applied to each argument.

def add_five(x):
    return x+5

nums = [1,2,3,4,5]

#result = list(map(add_five,nums))

result = list(map(lambda x:x+5,nums))

print(result)

