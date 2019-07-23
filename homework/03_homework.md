# 03_homework

## 01_문제

```python
# 1. built-in-function

print(dir(__builtins__))
# abs(), all(), bool(), float(), str()

```



## 02_문제

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

(1) ssafy(location='대전', name='철수')
(2) ssafy('길동', location='대전')
(3) ssafy(name='허준', '구미')

# 정답 : 3
# 키워드 변수는 뒤에 적어야 됨
```



## 03_문제

```python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(4, 7)
print(result)    
# 11
# None


```


