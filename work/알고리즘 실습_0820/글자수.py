import sys
sys.stdin = open('글자수_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = input()

    dic = {str1[i]: 0 for i in range(len(str1))}
    print(dic)

    for key in dic.keys():
        print(key)
        for s in str2:
            if key == s:
                dic[key] +=1
    print(dic)

    max = 0
    for value in dic.values():
        if max < value:
            max = value
    print('#{} {}'.format(tc,max))