import sys
sys.stdin = open('파리퇴치_input.txt')

T = int(input())
for tc in range(1, T+1):
    b, c = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(b)]
    # print(data)
    max = 0


    for i in range(c):
        for j in range(c):
            max += data[i][j]




    for i in range(b-c+1):
        for j in range(b-c+1):
            # data[i][j]
            sum1 = 0
            for x in range(c):
                for y in range(c):
                    sum1 += data[i+x][j+y]
            if max < sum1:
                max = sum1
    print("#{} {}".format(tc,max))


