# 1번 문제
# n = 5
# m = 9

# for i in range(m):
#    print('*' * n)

# n = 5
# m = 9
# for i in range(m):
#     for j in range(n):
#         print('*', end='')
#     print('')    


# 2번 문제
# student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
# sum = 0
# average = 0
# for value in student.values():
#     sum = sum + value
# average = sum / len(student)
# print(average)


# 3. 문제
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

dict = {}
# dict = {'A': 1}
# dict = {'A': 1. 'B': 1}\
# dict = {'A': 2, 'B': 1}
for i in blood_types:
    if dict.get(i):
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)                