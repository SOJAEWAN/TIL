# {1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 구하시오

import sys
sys.stdin = open('부분집합_input.txt')
data = list(map(int, input().split()))
A = [0 for _ in range(len(data))]

count = 0

def sumcheck(n):
    global count
    set = []
    for i in range(len(data)):
        if A[i] == 1:
            set.append(data[i])
    if sum(set) == 10:
        count += 1
        print('{} : {}' .format(count,set))


def powerset(n,k):
    global total
    if n == k:
        sumcheck(n)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

powerset(len(data), 0)
