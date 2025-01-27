def my_min(x,y,*args):
    
    min = x if x<y else y

    for i in args:
        if i<min:
            min=i
    return min        
print(my_min(8,1,3,42,10,0))     
