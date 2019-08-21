import sys
sys.stdin = open('문자열 비교_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()

    P = len(N) # 4
    Q = len(M) # 10


    def bruteForce2(text, pattern):
        for i in range(Q - P + 1): # 0 1 2 3 4 5 6
            cnt = 0
            for j in range(P): # 0 1 2 3
                if M[i+j] != N[j]:
                    break
                else: cnt +=1
            if cnt >= P:
                return 1
        return 0
    print('#{} {}'.format(tc,bruteForce2(N,M)))