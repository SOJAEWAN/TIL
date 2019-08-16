import sys
sys.stdin = open("구간합_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    b, c = map(int, input().split())
    lis = list(map(int, input().split()))

    max = 3
    min = 987654321

    for i in range(b-c+1):
        sum1 = 0

        for j in range(c):
            sum1 = sum1 + lis[i+j]

        if max < sum1:
            max = sum1


        if min > sum1:
            min = sum1


    print('#{} {}'.format(test_case, max-min))