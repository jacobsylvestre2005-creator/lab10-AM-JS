# https://github.com/jacobsylvestre2005-creator/lab10-AM-JS
# Partner 1: Jacob Sylvestre
# Partner 2: Avi McCarthy 

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)
    except ValueError as error:
        print(error)
        raise

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError as error:
        print(error)
        raise 
          
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def subtract(a, b):
    return sub(a, b)

def mul(a, b):
    return a * b

def multiply(a, b):
    return mul(a, b)

def div(a, b):
    match a:
        case 0:
            raise ZeroDivisionError
        case _:
            return b / a
        
def divide(a, b):
    return div(a, b)

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    else:
        return math.log(b, a)
    
def logarithm(a, b):
    if b <= 0 or a <= 0 or b == 1:
        raise ValueError("Log not defined for these inputs")
    return math.log(a, b)

def exp(a, b):
     return a ** b
 
def exponent(a, b):
    return exp(a, b)