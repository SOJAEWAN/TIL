# 05_workshop

## 01_문제

```python
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
```



## 02_문제

```python
import calc

val1 = int(input())
val2 = int(input())

print(calc.plus(val1, val2))
print(calc.minus(val1, val2))
print(calc.multiple(val1, val2))
print(calc.divisition(val1, val2))
```

![1563872192885](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563872192885.png)