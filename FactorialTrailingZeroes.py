def trailingZeroes( n: int) -> int:
    start = 5
    countZeros = 0
    while n//start:
        countZeros += n//start
        start *= 5
    
    return countZeros

print(trailingZeroes(30))