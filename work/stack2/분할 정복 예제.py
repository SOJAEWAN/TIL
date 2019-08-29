def power(base, exponent):


    result = 1 # base의 0승은 1이므로
    for i in range(exponent):
        result *= base
    return result

print(power(2,10))