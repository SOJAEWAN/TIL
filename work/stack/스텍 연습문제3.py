import sys
sys.stdin = open('스택 연습문제3_input.txt')

def dfs(start):
    visited[start] = 1
    print(start, end=" ")

    for w in range(1, V+1):
        if G[start][w] ==1 and visited[w] == 0:
            dfs(w)




V, E = map(int, input().split()) # 정점(b), 간선(c)
temp = list(map(int, input().split()))
G = [[0 for i in range(V+1)] for j in range(V+1)] # 2차원 초기화
visited = [0 for i in range(V+1)]


for i in range(0,len(temp),2): # 입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(V+1): # 입력확인
    print("{} {}".format(i, G[i]))
dfs(1)

print(visited)
