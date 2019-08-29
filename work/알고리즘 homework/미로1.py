import sys
sys.stdin = open('미로1_input.txt')


def dfs(x, y):
    global result
    visit[y][x] = 1

    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > 16 or ny > 16:
            continue

        if arr[ny][nx] == 1 or visit[ny][nx] == 1:
            continue

        if arr[ny][nx] == 3:

            result = 1

        dfs(nx, ny)

T = 10
for tc in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visit = [[0 for col in range(16)] for row in range(16)]
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    result = 0

    for i in range(0, 16):
        for j in range(0, 16):
            if arr[i][j] == 2:
                dfs(j,i)

    print('#{} {}'.format(tc,result))


