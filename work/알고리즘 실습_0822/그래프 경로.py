def dfs(v):
    global flag
    visit[v] = 1

    if v == g:
        flag = 1
        return

    for w in range(V+1):
        if G[v][w] == 1 and visit[w] == 0:
            dfs(w)


import sys
sys.stdin = open('그래프 경로_input.txt')

T = int(input())
for tc in range(1, T+1):
    V, e = map(int, input().split())
    G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    visit = [0 for i in range(V + 1)]
    flag = 0
    for i in range(e):
        info_v_x,info_v_y = map(int,input().split())
        G[info_v_x][info_v_y] = 1


    s, g = map(int, input().split())




    # for i in range(0, len(info_v), 2):
    #     G[info_v[i][0]][info_v[i][1]] = 1
    # # print(G)

    dfs(s)
    # if g in stack:
    #     result = 1
    # else:
    #     result = 0
    print('#{} {}'.format(tc, flag))
