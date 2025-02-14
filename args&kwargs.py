# Python allows you to have functions with varying numbers of arguments.

# Using *args as a function parameter enables you to pass an arbitrary 
# number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.

def function(named_arg,*args):
    print(named_arg)
    print(args)

function(1,2,3,4,5)    