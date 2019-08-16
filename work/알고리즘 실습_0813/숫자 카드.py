import sys
sys.stdin = open("숫자 카드_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    a = int(input())
    h = input()
    h1 = int(h)
    c = [0] * 10

    for i in range(0, len(h)):
        c[h1 % 10] += 1
        h1 //= 10

    max = c[0]
    for i in range(1, len(c)):
        if max < c[i]:
            max = c[i]

    for i in range(len(c)-1,-1,-1):
        if c[i] == max:
            val = i
            break


    print('#{} {} {}'.format(test_case, i, max))





