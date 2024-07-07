def lemonadeChange(bills):
    tenDollar = 0
    fiveDollar = 0

    for bill in bills:
        if bill == 5:
            fiveDollar += 1
        elif bill == 10:
            if fiveDollar >= 1:
                fiveDollar -= 1
                tenDollar += 1
            else:
                return False
        else:
            if tenDollar >= 1 and fiveDollar >= 1:
                fiveDollar -= 1
                tenDollar -= 1
            elif fiveDollar >= 3:
                fiveDollar -= 3
            else:
                return False
    return True

consoleInput = input("Enter lemanade queue array: ")
bills = [int(n) for n in consoleInput.split()]

print(lemonadeChange(bills))

    