import sys
sys.stdin = open('최대 사각 테두리 합.txt')

T = int(input())
for tc in range(1, T+1):
    A,B,C = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(A)]
    print(data)
    max = 0
    sum = 0
    for i in range(C-B+1):
        for j in range(C-B+1):
            
