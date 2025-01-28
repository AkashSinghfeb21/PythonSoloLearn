class Shape:
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w*self.h

    def __add__(self,other):
        return Shape(self.w+other.w,self.h+other.h)

    def __gt__(self,other):
        return self.area()>other.area()

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)        