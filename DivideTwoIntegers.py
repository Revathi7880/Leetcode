def divide(dividend: int, divisor: int) -> int:
    sign = 1
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) :
        sign = -1

    n = abs(dividend)
    d = abs(divisor)
    quotient = 0

    while n >= d:
        power = 0
        while n >= (d<<(power + 1)):
            power += 1
        
        quotient += 1<<power
        n -= (d<<power)

    if sign == 1 and quotient > 2**31 - 1:
        return 2**31 - 1
    elif sign == -1 and -quotient < -2**31:
        return -2**31
    else:
        if sign == 1:
            return quotient
        else: 
            return -quotient
        
print(divide(64683487, 34))


    
    