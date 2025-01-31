# Properties provide a way of customizing access to instance attributes. 

# They are created by putting the property decorator above a method, 
# which means when the instance attribute with the same name as the method is accessed, 
# the method will be called instead. 

# One common use of a property is to make an attribute read-only.

class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings
    @property
    def pineapple_allowed(self):
        return False

p = Pizza(["cheese","tomato"])
print(p.pineapple_allowed)
#p.pineapple_allowed = True       