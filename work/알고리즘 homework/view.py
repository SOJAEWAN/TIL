import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(T):
    N = int(input()) # 100개
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(2, len(arr)-2):
        cnt = 0
        h = 0
        for j in range(-2, 3):
            if j !=0:
                if arr[i] > arr[i + j]:
                    cnt += 1
                    if arr[i+j] > h:

                        h = arr[i+j]
        if cnt == 4:
            ans += arr[i] -h

    print("#{} {}".format(tc+1, ans))