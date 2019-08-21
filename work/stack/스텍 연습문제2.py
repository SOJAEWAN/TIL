s = list()
def isEmpty():
    if len(s) == 0:return True

    else: return False






def check_matching(data):
    for i in range(len(data)):
        if data[i] == '(':
            s.append('(')
        elif data[i] == ')':
            if isEmpty():
                return False
            else:
                s.pop()

    if not isEmpty(): return False
    else: return True





data = input()
print(check_matching(data))