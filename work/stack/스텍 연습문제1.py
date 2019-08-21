stack = []
top = -1

stack.append(1)
top += 1
stack.append(2)
top += 1
stack.append(3)
top += 1
print(stack)

print(stack.pop())
top -= 1

print(stack)
print(stack.pop())
top -= 1

print(stack)
print(stack.pop())
top -= 1

print(stack)