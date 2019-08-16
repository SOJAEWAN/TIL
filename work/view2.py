import sys
sys.stdin = open("view2_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    b = int(input())  # 100개
    c = list(map(int, input().split()))

    min = c[0]
    max = c[0]
    lis = []
    for i in range(1, len(c)):
        if max < c[i]:
            max = c[i]
    lis.append(max)

    for i in range(1, len(c)):
        if min > c[i]:
            min = c[i]
    lis.append(min)

    val = (lis[0] - lis[1])
    print('#{} {}'.format(test_case, val))