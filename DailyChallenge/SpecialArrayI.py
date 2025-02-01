def isArraySpecial(nums) -> bool:
    def isEven(n):
        if n%2 == 0:
            return True
        return False

    nLen = len(nums)
    for i in range(nLen-1):
        firstNum = isEven(nums[i])
        secondNum = isEven(nums[i+1])

        if firstNum == secondNum:
            return False
    return True

print(isArraySpecial([2,1,4]))