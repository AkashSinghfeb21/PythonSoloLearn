# Python also provides magic methods for comparisons.

# __lt__ for <

# __le__ for <=

# __eq__ for ==

# __ne__ for !=

# __gt__ for >

# __ge__ for >=

#  If __ne__ is not implemented, it returns the opposite of __eq__. 

# There are no other relationships between the other operators.

class SpecialString:
    def __init__(self,cont):
        self.cont = cont

    def __gt__(self,other):
        for i in range(len(other.cont)+1):
            result = other.cont[:i]+">"+self.cont
            result +=">"+other.cont[i:]
            print(result)

s=SpecialString("soap")
e=SpecialString("shampoo")
s>e