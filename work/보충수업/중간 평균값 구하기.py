import sys
sys.stdin = open('중간 평균값 구하기_input.txt')


T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    # print(data)
    max = data[0]
    min = data[0]

    for i in data:
        if max < i:
            max = i


    for i in data:
        if min > i:
            min = i


    sum = 0
    for i in data:
        sum += i
    aver = (sum - (max + min)) / (len(data)-2)
    print('#{} {}'.format(tc, round(aver)))