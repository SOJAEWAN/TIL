import sys
sys.stdin = open('반복문자 지우기_input.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(input())
    # print(data)
    stack = []

    for i in range(len(data)):
        if len(stack) == 0:
            stack.append(data[i])
        else:
            if stack[-1] == data[i]:
                stack.pop()
            else:
                stack.append(data[i])


    print('#{} {}'.format(tc, len(stack)))
