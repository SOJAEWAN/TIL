# val = int(input())
# result = 0

# def sgrt(s, e, count):
#     if val < s*s or val > e*e:
#         return
#     if count > 11:
#         global result
#         result= (s + e) / 2
#         return
#     sgrt(s, (s+e)/2, count+1)
#     sgrt((s+e)/2, e, count+1)

# for i in range(1,val):
#     if i * i > val:
#         sgrt(i-1, i, 0)
#         break
#     elif i * i == val:
#         result = i
#         break
# print(result)

def my_sqrt(n):
    x, y = 1, n # 양의 정수 -> 1부터  n까지
    result = 1 # 우리가 추측하는 제곱근의 근사값
    
    #while not math.isclose(result ** w, n):
    while abs(result**2 - n) > 0.0000000001:
        # 제곱근의 제곱과 입력 값의 차이가 적어도 0.000000001보다 작아지면 그 차이가 
        # 거의 없다 봄
        
        result = (x + y) / 2
        # 양쪽 끝 값의 절반을 다시 제곱근의 근사치로 둠
       
        if result ** 2 < n:
            x = result

        else:
            y = result
    return result      
print(my_sqrt(2))  

import math
print(math.sqrt(2))
