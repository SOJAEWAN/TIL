import sys
sys.stdin = open('Ladder1_input.txt')





for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visit = [[0 for col in range(100)] for row in range(100)]
    dx = [0, 0, -1]
    dy = [1, -1, 0]

    x = 99
    y = 0
    for i in range(0, 100):
        if arr[x][i] == 2:
            y = i
    result = 0
    isEnd = False
    while True:

        for i in range(0, 3):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0 or ny >= 100:
                continue
            if nx <= 0:
                # 게임 끝
                result = ny
                isEnd = True
                break
            if arr[nx][ny] == 0 or visit[nx][ny] == 1:
                continue;
            visit[nx][ny] = 1
            x = nx
            y = ny
            break;
        if isEnd == True:
            break
    # print("#" + str(T) + " " + str(result))
    print('#{} {}'.format(tc,result))