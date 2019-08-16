import sys
sys.stdin = open("금속막대_input.txt")
T = int(input())
for tc in range(1, T+1):
   N = int(input())
   bolts = list(map(str, input().split()))
   for i in range(N):
       for j in range(N):
           if bolts[i*2] == bolts[j*2+1]:
               break
           if j == N-1:
               startpoint = i*2
   sumbolts = [bolts[startpoint], bolts[startpoint+1]]
   count = 1
   while 1:
       for i in range(N):
           if sumbolts[-1] == bolts[i*2]:
               sumbolts.append(bolts[i*2])
               sumbolts.append(bolts[i*2+1])
               count += 1
       i = 0
       if count == N:
           break
   print('#{} {}'.format(tc, ' '.join(sumbolts)))

