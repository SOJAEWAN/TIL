# 07_homework

```python
class Calculator:
    count = 0
    def info(self):
        print('나는 계산기 입니다.')


    @staticmethod
    def add(a, b):
        Calculator.count += 1
        print(f'{a} + {b} 는 {a + b} 입니다.')

    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')
```



## 01_문제

```python
# 1. 
# 인스턴드 메서드 : info()
# 스태틱 메서드 : add()
# 클래스 메서드 : history()
```



## 02_문제

```python
# 2.
# 인스턴스 메서드
# c = Calculator
# c.info()

# 스태틱 메서드
# Calculator.add(1, 2)
# Calculator.add(3, 4)

# 클래스 메서드
# Calculator.history()
```



## 03_문제

```python
# 3.
# self: 인스턴스(calculator)
# cls : 클래스(calculator)
```

