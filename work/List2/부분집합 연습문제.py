import sys
sys.stdin = open('부분집합 연습문제_input.txt', 'r')
sum = 0
arr = list(map(int, input().split()))
for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j): sum += arr[j]
    cnt = 0
    count = 0
    if sum == 10:
        for j in range(len(arr)):
            if i & (1 << j):
                cnt += 1
                sum += arr[j]

            if cnt == 3 and sum == 6:
                count += 1


                print(arr[j], end=' ')
        print()