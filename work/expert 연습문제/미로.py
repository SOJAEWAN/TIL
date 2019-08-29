import sys
sys.stdin = open('미로_input.txt')


def dfs(x,y):
    global result
    visit[y][x] = 1

    for v in range(0, 4):
        nx = x + dx[v]
        ny = y + dy[v]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if arr[ny][nx] == 1 or visit[ny][nx] == 1:
            continue

        if arr[ny][nx] == 3:
            result = 1

        dfs(nx,ny)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visit = [[0 for col in range(N)] for raw in range(N)]
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(0, N):
        for j in range(0, N):
            if arr[i][j] == 2:
                dfs(j,i)

    print('#{} {}'.format(tc, result))