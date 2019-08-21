import sys
sys.stdin = open('회문2._input.txt')

T = 10
for tc in range(1, T+1):
    test = int(input())
    data = [list(input()) for _ in range(100)]

    result = 0
    chk = 0
    for N in range(100, 0, -1): # N:
        for i in range(100): # i: 행선택길이
            for j in range(100 - N + 1): # j: 시작지점
                word = data[i][j:j+N] # 시작지점에서 N만큼. 슬라이싱.
                for v in range(len(word) // 2): #
                    if word[v] != word[-1 - v]:
                        break
                    if v == (len(word) // 2 - 1):
                        result = len(word)
                        chk = 1
                if chk:
                    break
            if chk:
                break
        if chk:
            break

    chk = 0

    for N in range(100, 0, -1):
        for i in range(100 - N + 1):
            for j in range(100):
                lis = []
                for m in range(N):
                    lis.append(data[i+m][j])
                for v in range(len(lis) // 2):
                    if lis[v] != lis[-1 - v]:
                        break
                    if v == (len(lis) // 2 - 1):
                        if result < len(lis):
                            result = len(lis)
                            chk = 1
                            break
                        else:
                            chk = 1
                            break
                if chk:
                    break
            if chk:
                break
        if chk:
            break
    print('#{} {}'.format(tc,result))