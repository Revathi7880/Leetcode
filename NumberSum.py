def numberSum(n):
    num = n
    sum = 0
    while num > 0:
        rem = num % 10 
        sum += rem
        num = int(num / 10)

    return sum

print(numberSum(29))