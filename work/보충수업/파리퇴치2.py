import sys
sys.stdin = open('파리퇴치_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    max = 0


    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for x in range(M):
                for y in range(M):
                    sum += arr[i+x][j+y]

            if max < sum:
                max = sum

    print("#{} {}".format(tc, max))