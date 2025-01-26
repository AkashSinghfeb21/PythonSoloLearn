t = [('James',42),('Amy',36),('John',24),
     ('Amanda',63),('Bob',18)]

n = input()

for name,age in t:
    if(name==n):
        print(f"{name} is {age}")
        break

else:
    print("Not found")