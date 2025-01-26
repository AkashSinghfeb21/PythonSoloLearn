def is_Prime(x):
    if x<2:
        return False
    elif x==2:
        return True
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def PrimeGenerator(x,y):
    for i in range(x,y):
        if is_Prime(i):
            yield i

f = int(input())
t = int(input())

print(list(PrimeGenerator(f,t)))