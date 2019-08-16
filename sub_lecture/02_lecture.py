"""
n개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 값이 몇번째 수 인지 구하세요.

예를 들어, 서로 다른 n개의 자연수가 [3, 29, 38, 12, 57, 74, 40, 85, 61]
이라면 최대값은 85, 7번째 수

answer = [85, 7]
"""
lis = [3, 29, 38, 12, 57, 74, 40, 85]
max_num = lis[0]
result = []
for i in range(1, len(lis)):
    result = []
    if max_num < lis[i]:
        max_num = lis[i]
    result.append(max_num)
    result.append(lis.index(max_num))

print(result)

    
