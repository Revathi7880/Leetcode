def passThePillow(n, time):
    passCount = time
    if time > 2*(n - 1):
        passCount = time % (2*(n - 1))

    if passCount < n:
        return passCount + 1
    else:
        difference = passCount - n
        return n - difference - 1
    
n = int(input("Enter the n value: "))
time = int(input("Enter the time: "))
print(passThePillow(n, time))

        