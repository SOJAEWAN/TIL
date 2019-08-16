def positive_sum(numbers):
    """
    여기에 코드를 작성하시오.
    numbers는 숫자들이 담긴 리스트입니다.
    numbers에 담긴 숫자들 중, 양의 정수들의 합을 반환합니다.
    """
    sum = 0
    for i in numbers:
        if i > 0:
            sum = i + sum
    return sum

print(positive_sum([1, -4, 7, 12]))
print(positive_sum([-1, -2, -3, -4]))
