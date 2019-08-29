import sys
sys.stdin = open("종이붙이기_input.txt")
def paper(N):
   global count
   if N <= 10:
       return 1
   else:
       return paper(N - 10) + 2 * paper(N - 20)

T = int(input())
for tc in range(1, T+1):
   N = int(input())
   print('#{} {}'.format(tc, paper(N)))