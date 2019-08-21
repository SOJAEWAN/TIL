import sys
sys.stdin = open('회문_input.txt')

T = int(input())
for tc in range(1, T+1):
    b,c = map(int, input().split())
    val = [list(input()) for _ in range(b)]
    print(val)
    result = []
    for i in range(b):
        for j in range(b-c+1):
            word = val[i][j:j+c]
            for v in range(len(word) // 2):
                if word[v] != word[-1 - v]:
                    break
                if v == (len(word) // 2 - 1):
                    result = word

    for i in range(b):
        for j in range(b-c+1):
            word1 = []
            for m in range(c):
                word1.append(val[j+m][i])

            for v in range(len(word1) // 2):
                if word1[v] != word1[-1 - v]:
                    break
                if v == (len(word1) // 2 - 1):
                    result = word1

    print("#{} {}".format(tc, ''.join(result)))