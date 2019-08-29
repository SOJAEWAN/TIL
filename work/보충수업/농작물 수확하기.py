import sys
sys.stdin = open('농작물 수확하기_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    print(data)

    startpoint = 1
    endpoint = data[N-1][N//2]
    middle_sum = 0
    for i in range(N):
        middle_sum += data[N // 2][i]


    for i in range(1, N+1, 2): # N이 5일때 i= 1, 3, 5
        if (i-startpoint) //2 ==0:
            sum += startpoint
        if (i - startpoint)//2 ==




    for i in range(N):
        for j in range(N):
