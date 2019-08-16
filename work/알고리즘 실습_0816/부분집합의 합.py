import sys
sys.stdin = open('부분집합의 합_input.txt')


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
val = []

for i in range(1, 1 << len(arr)):
    val1 = []
    for j in range(len(arr)):
        if i & (1 << j):
            val1.append(arr[j])
    val.append(val1)

print(val)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0

    for v in val:
        sum = 0

        if len(v) == N:
            for m in range(N):
                sum += v[m]

        if sum == K:
            cnt += 1

    print("#{} {}".format(tc, cnt))







