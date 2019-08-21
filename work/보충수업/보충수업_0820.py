# 자연수 n을 입력받아서 n개의 줄에 n+1개의 숫자 혹은 문자로 채워서 다음과 같이 출력하는 프로그램을 작성하시오.


# 1 2 3 A
# 4 5 B C
# 6 D E F
#
# n = int(input())
# digit = 1
# alpha = 'A'
#
# for i in range(n): # i = 0 1 2
#     for j in range(n-i,0,-1): # n=3일때 i=0, 3 2 1   i=1, 2 1    i=2, 1
#         print(digit, end=' '),
#         digit += 1
#     for k in range(i + 1):
#         print(alpha, end=' '),
#         ch2 = ord(alpha) + 1
#         alpha = chr(ch2)
#     print("")


n