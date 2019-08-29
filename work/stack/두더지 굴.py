import sys
sys.stdin = open('두더지 굴_input.txt')


N = int(input())
data1=[list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if data1[ny][nx] == 0 or visit[ny][nx] != 0:
            continue

        visit[ny][nx] = 1
        dfs(nx, ny)

cnt = 0

for i in range(N):
    for j in range(N):
        if data1[i][j] != 0 and visit[i][j] == 0:
            visit[i][j] = 1
            dfs(j, i)
            cnt += 1

print(cnt)