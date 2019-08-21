# 1. 
# built-in-function
# print(dir(__builtins__))
# abs(), all(), bool(), float(), str()

# 2. 
# def ssafy(name, location='서울'):
#     print(f'{name}의 지역은 {location}입니다.')

# ssafy(location='대전', name='철수')
# ssafy('길동', location='대전')
# ssafy(name='허준', '구미')
# #정답 :  3
# # 키워드 변수는 뒤에 적어야 됨

# # 3.
# def my_func(a, b):
#     c = a + b
#     print(c)

# result = my_func(4, 7)
# print(result)    
# None

# i = 7
# for i in range(i,0,-2):
#     print(' ' * (4-(i//2)), end='')
#     print('*' * i)

# val = int(input())
# for i in range(1, val+1):
#     if val%i == 0:
#         print(f'{i}(은)는 {val}의 약수입니다.')
