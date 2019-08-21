import sys
sys.stdin = open('GNS_input.txt')

T = int(input())
for tx in range(1, T+1):
    tc, N = input().split()
    num = int(N)
    data = input().split()
    # print(data)
    # print(data[0])

    for i in range(num):
        if data[i] == "ZRO":
            data[i] = 0
        if data[i] == "ONE":
            data[i] = 1
        if data[i] == "TWO":
            data[i] = 2
        if data[i] == "THR":
            data[i] = 3
        if data[i] == "FOR":
            data[i] = 4
        if data[i] == "FIV":
            data[i] = 5
        if data[i] == "SIX":
            data[i] = 6
        if data[i] == "SVN":
            data[i] = 7
        if data[i] == "EGT":
            data[i] = 8
        if data[i] == "NIN":
            data[i] = 9
    data1 = sorted(data)

    for j in range(num):
        if data1[j] == 0:
            data1[j] = "ZRO"
        if data1[j] == 1:
            data1[j] = "ONE"
        if data1[j] == 2:
            data1[j] = "TWO"
        if data1[j] == 3:
            data1[j] = "THR"
        if data1[j] == 4:
            data1[j] = "FOR"
        if data1[j] == 5:
            data1[j] = "FIV"
        if data1[j] == 6:
            data1[j] = "SIX"
        if data1[j] == 7:
            data1[j] = "SVN"
        if data1[j] == 8:
            data1[j] = "EGT"
        if data1[j] == 9:
            data1[j] = "NIN"

    print("#{}".format(tx))

    for k in data1:
        print(k, end=" ")

    print()

