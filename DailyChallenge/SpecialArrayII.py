def isArraySpecial(nums, queries):
    def isEvenorOdd(n):
        return "even" if n%2 == 0 else "odd"
    
    def binarySearch(q, specialList):
        left, right = 0, len(specialList) - 1
        while left <= right:
            mid = (left + right) // 2
            if q >= specialList[mid][0] and q <= specialList[mid][1]:
                return mid
            elif q < specialList[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

    specialList = []
    subArray = []
    previousParity = ""
    for i in range(len(nums)):
        result = isEvenorOdd(nums[i])
        if not previousParity:
            subArray.append(i)
        else:
            if result == previousParity:
                subArray.append(i - 1)
                specialList.append(subArray)
                subArray = [i]
        previousParity = result
    if subArray:
        subArray.append(len(nums) - 1)
        specialList.append(subArray) 
    print(specialList)
    
    qBool = []
    for q in queries:
        indexOfStart = binarySearch(q[0], specialList)
        indexOfEnd = binarySearch(q[1], specialList)
        if indexOfStart == indexOfEnd:
            qBool.append(True)
        else:
            qBool.append(False) 

    return qBool

print(isArraySpecial([4,3,1,6],[[0,2],[2,3]]))


        

    