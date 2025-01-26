# Due to the fact that they yield 
#one item at a time, generators 
#don't have the memory restrictions of lists. 

# In fact, they can be infinite!

def infinite_sevens():
    while True:
        yield 7

for i in infinite_sevens():
    print(i)