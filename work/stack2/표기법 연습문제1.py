import sys
sys.stdin = open('표기업 연습문제_input.txt')

data = list(input())
stack = []
for i in range(len(data)):
    if not data[i] in '+-*/':
        print(data[i], end=' ')
    else:
        stack.append(data[i])

while len(stack) != 0:
    print(stack.pop, end=' ')