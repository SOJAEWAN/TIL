# import calc
# val1 = int(input())
# val2 = int(input())

# print(calc.plus(val1, val2))
# print(calc.minus(val1, val2))
# print(calc.multiple(val1, val2))
# print(calc.divisition(val1, val2))

for i in range(1, 10):
    print(f'-------[{i}단]-------')
    for j in range(2, 10):
        print(i, "*", j, "=", i*j)