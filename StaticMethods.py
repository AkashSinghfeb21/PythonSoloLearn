# Static methods are similar to class methods, 
# except they don't receive any additional arguments; 
# they are identical to normal functions that belong to a class. 

# They are marked with the staticmethod decorator.

class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
    def __str__(self):
        return f"[{','.join(self.toppings)}]" 
    
       
ingredients = ["cheese","onions","spam"]

try: 
   if all(Pizza.validate_topping(i) for i in ingredients):
      pizza = Pizza(ingredients)
      print(pizza)
except ValueError as e:
      print(f"Error:{e}")         

        

