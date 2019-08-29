ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scraping": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "justin",
            "manager": "pro-gm",
            "class president": "고승연",
            "groups": {
                "A": ["강민구", "고승연", "권대민", "김가영", "김도훈"],
                "B": ["김정덕", "김평강", "남수경", "류재헌", "박교열"],
                "C": ["박찬환", "배태한", "백서현", "변인욱", "서혜영"],
                "D": ["소재완", "유일규", "윤명훈", "이은수", "이지훈"],
                "E": ["이현우", "임현수", "정성훈", "평준혁", "하승진"]
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}
# val = len(ssafy.get("location"))
# print(val)

# print('request' in ssafy.get("language").get("python").get("python standard library"))

# val = ssafy.get("classes").get("gm").get("class president")
# print(val)

# for key in ssafy["language"].keys():
#     print(key)

# for value in ssafy["classes"]["gj"].values():
# #     print(value)
#
#
# user_list = ['john', 'paul', 'george', 'ringo']
# val = input()
#
# if val in user_list:
#     password = int(input())
#     if password == 12345678:
#         print('환영합니다.')
#     else:
#         print('비밀번호가 틀렸습니다.')
# else:
#     print('존재하지 않는 사용자입니다.')
#

# val = 1000
# r = 0.05
# num = int(input())
# while val * ((1 + r) ** num) <= 2000:
#     num += 1
#     print(num)



# def func(n):
#     if n==1:
#         return 1
#     else:
#         return n * func(n-1)
# func(4)
# print(func(4))



# for i in range(1, 10):
#     print(f'-----[{i}단]-----')
#     for j in range(2, 10):
#         print(f'{i} '*' {j} '=' {i}*{j}')

# val = input()
# cnt = 0
# vnt = 0
# for i in val:
#     if i in 'aieou':
#         cnt += 1
#     else:
#         vnt += 1
# print('vowels =', end= ' ')
# print(cnt)
# print('constants =', end= ' ')
# print(vnt)

#
# def positive_sum(numbers):
#     """
#     여기에 코드를 작성하시오.
#     numbers는 숫자들이 담긴 리스트입니다.
#     numbers에 담긴 숫자들 중, 양의 정수들의 합을 반환합니다.
#     """
#     sum = 0
#     for i in numbers:
#         if i > 0:
#             sum = i + sum
#     return sum
#
# print(positive_sum([1, -4, 7, 12]))
# print(positive_sum([-1, -2, -3, -4]))
#
#
# def calc(equation):
#     """
#     아래에 코드를 작성하시오.
#     equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
#     계산된 결과를 정수로 반환합니다.
#     """
#     val = [map(int, equation) for j in equation]
#     # list1 = equation.split()
#     sum = 0
#     for i in val:
#         sum = i + sum
#     return sum

# def calc(equation):
#     """
#     아래에 코드를 작성하시오.
# #     equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
# #     계산된 결과를 정수로 반환합니다.
# #
# #     """\
# def calc(equation):
#     # """
#     # 아래에 코드를 작성하시오.
#     # equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
#     # 계산된 결과를 정수로 반환합니다.
#     # """
#     val = equation.replace('-','+-')
#
#     val1 = val.split('+')
#
#     if val1[0] == '':
#         val1[0] = 0
#     val2 = list(map(int, val1))
#     return sum(val2)
#
#
#
# # 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
# # if __name__ == '__main__':
# print(calc('123+2-124'))
# print(calc('-12+12-7979+9191'))
# print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))


# def val(a,b):
#     if len(a) > len(b):
#         return a
#     else:
#         return b
# print(val('one', 'three'))
#

# def countdown(a):
#     if a <= 0:
#         print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
#     else:
#         for i in range(a, 0, -1):
#             print(i)
#
#     return
#
# countdown(0)
# countdown(10)

# from datetime  import datetime
# b = [input(), int(input())]
# date = datetime.today().year
# date += 100-b[1]
#
# print("{}(은)는 {}년에 100세가 될 것입니다.".format(b[0], date))
#
# a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
# print(sum(list(map(lambda x: (x=='A')*4,a))) + sum(list(map(lambda x: (x=='B')*3,a))) + sum(list(map(lambda x: (x=='C')*2,a))) + sum(list(map(lambda x: (x=='D')*1,a))))

# def val(*a):
#     b = 1
#     for i in a:
#         if type(i) != int:
#             return print('에러발생')
#
#         b = i*2
#     return print(b)
#
# val(1, 2, '4', 3)

# a = 65
# print('ASCII {} => {}'.format(a, chr(a)))


# print(list(filter(lambda x: x%2==0,range(1, 11))))

# print(list(map(lambda x: x**2, range(1, 11))))

# a =  list(filter(lambda x: x%2==0, range(1, 11)))
# print(list(map(lambda x: x**2, a)))

# def max_num(*a):
#     num = a[0]
#     for i in range(len(a)):
#         if num < a[i]:
#             num = a[i]
#     return num
#
# print('max_num(3, 5, 4, 1, 8, 10, 2) =>', end=" ")
# print(max_num(3, 5, 4, 1, 8, 10, 2))

# val = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}
# a = list(val.keys())
# b = list(val.values())
#
# for i in range(len(val)):
#     print('{}: {}'.format(a[i], b[i]))

for i1 in range(1, 4):
    for i2 in range(1,4):
        if i1 != i2:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2 :
                    print(i1, i2, i3)