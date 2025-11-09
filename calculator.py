import math 

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def log(a, b):
    if b <= 0 or a <= 0 or b == 1:
        raise ValueError("Log not defined for these inputs")
    return math.log(a, b)

def exp(a, b):
     return a ** b



