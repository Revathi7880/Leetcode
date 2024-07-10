def reverse(x):
    if x == 0:
        return 0
    numstr = str(abs(x))
    num = ''
    for i in reversed(numstr):
        num = num + i

    reverseNumber = int(num)

    if x < 0:
        if -reverseNumber < -(2**31):
            return 0
        return -reverseNumber
    else:
        if reverseNumber > 2**31:
            return 0
        return reverseNumber

x = int(input("Enter a number: "))
print(reverse(x))
    