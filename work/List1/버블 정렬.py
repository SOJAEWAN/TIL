def BubbleSort(a): #정렬할 LIST

    for i in range(len(a)-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] >a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] #swap
    return a
num = [55, 7, 78, 12, 42] #참조형(수정까지 가능)
print(BubbleSort(num))
# print(num)

def test():
    # global c
    c = 500
    print(c) # 읽기만 가능

c = 100 # 값형
test()
print(c)

