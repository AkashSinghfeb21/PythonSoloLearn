
# Decorators provide a way to modify functions 
#using other functions. 

# This is ideal when you need to extend 
#the functionality of functions that you don't want to modify.

def decor(func):
    def wrap(name):
    #def wrap():    
        print("------------")
        #func()
        func(name)
        print("------------")
    return wrap

# def print_text():
#     print("{Hello World}")

@decor
def Print_name(name):
    print(f"{name} is Great")    

# decorated = decor(print_text)

# decorated()
    
Print_name("Akash")    