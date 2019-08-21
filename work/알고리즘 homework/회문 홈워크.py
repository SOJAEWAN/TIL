import sys
sys.stdin = open('회문_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8 - N + 1):
            word = data[i][j:j+N]
            for v in range(len(word) // 2):
                if word[v] != word[-1 - v]:
                    break
                if v == (len(word) // 2 - 1):
                    cnt += 1


    for i in range(8):
        for j in range(8 - N + 1):
            lis = []
            for m in range(N):
                lis.append(data[j+m][i])
            # print(lis)


            for v in range(len(lis) // 2):
                if lis[v] != lis[-1 - v]:
                    break
                if v == (len(lis) // 2 - 1):
                    cnt += 1

    print("#{} {}".format(tc, cnt))