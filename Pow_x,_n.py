def myPow(x: float, n: int) -> float:
    positiveN = abs(n)
    res = 1
    while positiveN > 0:
        if positiveN % 2 == 1:
            res *=  x
            positiveN -= 1
        else:
            x *= x
            positiveN /= 2
    
    return res if n >= 0 else 1/res

print(myPow(2.00000, -2))


    