# Generators are a type of iterable, like lists or tuples. 

# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops. 

# They can be created using functions and the yield statement.


def countdown():
    i=5
    while(i>0):
        yield i
        i-=1

for i in countdown():
    print(i)