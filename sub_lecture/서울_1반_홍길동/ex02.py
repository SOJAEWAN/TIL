# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    val = equation.replace('-','+-')
    val1 = val.split('+')
    if val1[0] == '':
        val1[0] = 0
    val2 = list(map(int, val1))
    return sum(val2)




# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
# if __name__ == '__main__':
print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))