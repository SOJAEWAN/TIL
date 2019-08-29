import sys
sys.stdin = open('sum_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    sum = 0
    sum1 = 0
    for i in range(100):
        sum += data[i][i]
        sum1 += data[i][99-i]

    if sum < sum1:
        result = sum
    else: result = sum1
    # print(result)

    result1 = 0
    max = 0

    for i in range(100):
        sum2 = 0
        for j in range(100):
            sum2 += data[i][j]
            if max < sum2:
                max = sum2

    max1 = 0
    for i in range(100):
        sum3 = 0
        for j in range(100):
            sum3 += data[j][i]
            if max1 < sum3:
                max1 = sum3

    if max < max1:
        result1 = max1
    else:
        result1 = max
    # print(result1)

    final_max = 0
    if result < result1:
        final_max = result1
    else:
        final_max = result

    print('#{} {}'.format(tc, final_max))


