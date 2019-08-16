import sys
sys.stdin = open('이진탐색_input.txt')

T = int(input())

for tc in range(1, T+1):
    P, *page = map(int, input().split())

    cnt = [0]*2
    for i in range(2):
        l, r = 1, P
        while True:
            c = (l + r)//2
            cnt[i] += 1

            if page[i] > c:
                l = c
            elif page[i] < c:
                r = c
            else:
                break

    if cnt[0] < cnt[1]:
        ans = 'A'
    elif cnt[0] > cnt[1]:
        ans = 'B'
    else:
        ans = 0

    print('#{0} {1}'.format(tc, ans))