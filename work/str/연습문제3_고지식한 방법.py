
def bruteForce(text, pattern):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i -j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return -1

def bruteForce2(text, pattern):
    for i in range(N - M):
        cnt = 0
        for j in range(M):
            if t[i+j] != p[j]:
                break
            else: cnt += 1
        if(cnt >= M): return i
    return -1


p = "TTA"  # 찾을 패턴
t = "TTTTAACCA"  # 전체 텍스트
M = len(p)  # 찾을 패턴의 길이
N = len(t)  # 전체 텍스트의 길이
print('{}'.format(bruteForce(t,p)))
print('{}'.format(bruteForce2(t,p)))
