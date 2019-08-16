import sys
sys.stdin = open("전기버스_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    Busstation = [0] * N + [0]
    for i in charge:
        Busstation[i] = 1
    noc = 0
    x = 0
    while x < len(Busstation):
        if x + K >= N:
            break
        else:
            for j in range(K, 0, -1):
                if Busstation[x + j] == 1:
                    x += j
                    noc += 1
                    break
            else:
                noc = 0
                break
    print('#{} {}'.format(test_case, noc))