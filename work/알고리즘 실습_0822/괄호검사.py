import sys
sys.stdin = open('괄호검사_input.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(input())
    stack = []

    start = ['(', '{', '[']
    end = [')', '}', ']']
    result = 1
    for i in range(len(data)):
        if data[i] in start:
            stack.append(data[i])
        if data[i] in end:
            if len(stack) == 0:
                result = 0
                break
            else:
                if start.index(stack[-1]) == end.index(data[i]):
                    stack.pop()
                else:
                    result = 0
                    break
    if len(stack) != 0:
        result = 0

    print('#{} {}'.format(tc,result))