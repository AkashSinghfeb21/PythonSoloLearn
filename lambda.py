# In Python, a lambda function is a small anonymous function that can take any number of arguments but can only have one expression. It is defined using the lambda keyword and is typically used for short, temporary functions 
# that do not require a formal function definition.

price = int(input())
percentage = int(input())

def perc(price,percentage):
    return price*percentage/100

result = (lambda x,y:x*y/100)(price,percentage)

print(result)
print(perc(price,percentage))