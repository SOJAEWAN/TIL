import sys
sys.stdin = open('칠 영역의 개수 구하기_input.txt')

T = int(input())
for tc in range(1, T+1):
    b,c = map(int, input().split())
    data = [list(map(int,input().split())) for _ in range(c)]
    # print(data)

    G = [[0 for _ in range(b)] for _ in range(b)]
    # print(G)


    for v in range(c):
        for dx in range(data[v][3]-data[v][1]+1):
            for dy in range(data[v][2]-data[v][0]+1):
                G[data[v][0]-1 +dy][data[v][1]-1 +dx] = 1


                    # G[data[i][k]][data[i][k] + j] = 1
    # for i in range(len(G)):
    #     print(G[i])

    cnt = 0
    for i in range(b):
        for j in range(b):
            if G[i][j] == 1:
                cnt += 1

    print("#{} {}".format(tc, cnt))