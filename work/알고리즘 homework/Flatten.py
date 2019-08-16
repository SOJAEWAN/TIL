import sys
sys.stdin = open("Flatten_input.txt")

T= 10
for tc in range(1, T+1):
    N = int(input())
    val = list(map(int, input().split()))

    for i in range(N):
        max = 1
        min = 100
        max_index = 0
        min_index = 0
        for j in range(100):
            if max < val[j]:
                max = val[j]
                max_index = j

            if min > val[j]:
                min = val[j]
                min_index = j

        val[max_index] -= 1
        val[min_index] += 1
# print(max-min)
        max = 1
        min = 100
        for j in range(100):
            if max < val[j]:
                max = val[j]
                max_index = j

            if min > val[j]:
                min = val[j]
                min_index = j

    print(max-min)


