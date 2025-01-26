def calc(x):
    #your code goes here
   p=4*x
   a=x*x

   return p,a 

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))