menu = ["Fries","Sandwich","CheeseBurger","Coffee","Soda"]

try:
    a=int(input())
    print(menu[a])
    print("Thanks for your order")
except (ValueError):
    print("Item Not Found")
except:
    print("Item Not Found")        