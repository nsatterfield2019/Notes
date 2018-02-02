'''
Function and Module Notes
v1.0
by Nathan Satterfield
'''
from random import *       # random is a library or module, * is the wildcard
from math import pi
# from math import *
import my_module
# imports go to the top of your program

# when you use keyword from, you are importing directly into your file
# (no need to use random.randrange, just use randrange)

# Functions and Modules


if __name__ == "__main__":
    '''
    This code only runs if this is the executed code/file.
    '''
    print(randrange(100))
    print(random())
    print(pi)
    
    e = 5
    print(e)
    print("This is period", my_module.period)
    my_module.hello("Nathan")
    product, sum = (my_module.product_sum(10, 20))
    print(product, sum)

    print(3, 4, sep = "," , end = "")
    print(5, 6)

    my_module.hello(name = "Francis")
    my_module.hello()