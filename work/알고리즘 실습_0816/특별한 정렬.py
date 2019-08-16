import sys
sys.stdin = open("특별한 정렬_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    val = list(map(int, input().split()))

    for i in range(N):

        for j in range(i, N):
            if i % 2 == 0:
                if val[i] < val[j]:
                    val[i], val[j] = val[j], val[i]

            else:
                if val[i] > val[j]:
                    val[i], val[j] = val[j], val[i]

    print('#{}'.format(tc), end=' ')
    for v in range(10):
        print(val[v], end=" ")
    print()
