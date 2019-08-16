import sys
sys.stdin = open("색칠하기_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0] * 10 for i in range(10)]
    cnt = 0

    for i in range(N):
        val = list(map(int, input().split()))


        if val[4] == 1:
            for x in range(val[0], val[2]+1):
                for y in range(val[1], val[3]+1):
                    if data[y][x] == 0:
                        data[y][x] = 1
                    elif data[y][x] == 2:
                        data[y][x] = 3
                        cnt += 1

        if val[4] == 2:
            for x in range(val[0], val[2]+1):
                for y in range(val[1], val[3]+1):
                    if data[y][x] == 0:
                        data[y][x] = 2
                    elif data[y][x] == 1:
                        data[y][x] = 3
                        cnt += 1

    print('#{} {}'.format(tc, cnt))