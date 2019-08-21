def plus(a, b):
    c = a + b
    return c
def minus(a, b):
    d = a - b
    return d
def multiple(a, b):
    e = a * b
    return e
def divisition(a, b):    
    try:
        f = a / b
    except ZeroDivisionError: 
        return '0으로는 나눌 수 없습니다'
    else:
        return f
