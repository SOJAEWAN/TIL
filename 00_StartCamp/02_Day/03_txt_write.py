#1. 파일 쓰기(옛날 방식)

# f = open('ssafy.txt', 'w')
# for i in range(10):
#     f.write(f'This is line {i}.\n')
# f.close()

#2. 파일 쓰기(최신 방식)

# with open('with_ssafy.txt', 'w') as f:
#     for i in range(10):
#         f.write(f'This is line {i}.\n')

with open('writelines_ssafy.txt', 'w') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])