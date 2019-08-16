#  100 이하의 양의 정수만 입력된다. while 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력하는 프로그램을 작성하시오.
#
# num = int(input())
# sum = 0
# n = 1
# while n <= num:
#     sum = sum + n
#     n += 1
# print(sum)



# 한 개의 정수를 입력받아 양수(positive integer)인지 음수(negative number)인지 출력하는 작업을 반복하다가 0이 입력되면 종료하는 프로그램을 작성하시오.
#
# * 입출력예의 진한글씨는 출력값입니다.​
#
# number? 10
# positive integer
# number? -10
# negative number
# number? 0

# num = int(input('number? '))
# while True:
#     if num > 0:
#         print('positive integer')
#     elif num < 0:
#         print('negative number')
#
#     else:
#         break
#     num = int(input('number? '))

#
#
# 정수를 계속 입력받다가 100 이상의 수가 입력이 되면 마지막 입력된 수를 포함하여 합계와 평균을 출력하는 프로그램을 작성하시오.
#
# (평균은 반올림하여 소수 첫째자리까지 출력한다.)
#
#
# 입력 예
# 1 2 3 4 5 6 7 8 9 10 100
#
# 출력 예
# 155
# 14.1


# num = input()
# num_str = num.split()
# sum = 0
# average = 0.0
# i = 0
# num_list = list(num_str)
#
# while True:
#     sum = sum + int(num_list[i])
#     i += 1
#     if int(num_list[i-1]) >= 100:
#         break
#
# print(sum)
# print(round(sum / len(num_str), 1))




# 정수를 입력받아서 3의 배수가 아닌 경우에는 아무 작업도 하지 않고 3의 배수인 경우에는 3으로 나눈몫을 출력하는 작업을 반복하다가 -1이 입력되면 종료하는 프로그램을 작성하시오.
#
# * 입출력예의 진한 글씨는 실행값이다.
#
#
#
# 입력 예
# 5
# 12
# 4
# 21
# 7
# 100
# -1


# while True:
#     num = int(input())
#     if num % 3 == 0:
#         print(num//3)
#
#     if num == -1:
#         break




