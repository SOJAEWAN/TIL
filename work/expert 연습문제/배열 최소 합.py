import sys
sys.stdin = open('배열 최소 합_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)
    min = 10


    for i in range(N):
        for j in range(N):
            if data[i][j]
