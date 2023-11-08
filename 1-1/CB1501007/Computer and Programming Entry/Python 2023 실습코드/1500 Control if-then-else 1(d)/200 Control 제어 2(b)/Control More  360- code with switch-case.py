
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate1(operator, x, y):
    cases = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    return cases[operator](x, y)

def calculate2(operator, x, y):
    cases = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    return cases[operator](x, y)

val = calculate1("+", 100, 312)
print( f'val= {val}')

val = calculate2("+", 10,  72)
print( f'val= {val}')






