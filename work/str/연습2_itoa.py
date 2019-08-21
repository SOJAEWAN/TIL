def itoa(x):
    lis = []
    while x != 0:
        a = x % 10
        x = x // 10
        lis.append(chr(a+48))
    lis.reverse()
    return ''.join(lis)
#
x = 123;
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))
# print(lis)