import sys
sys.stdin = open('문제2_input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(A)]
    print(data)
    max = 0

    sum = 0
    for i in range(A-C + 1):
        for j in range(B-C + 1):
            for x in range(C):
                for y in range(C):
                    sum += data[i+x][j+y]

    if max < sum:
        max = sum
    print(max)


