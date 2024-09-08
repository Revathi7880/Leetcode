def productExceptSelf(nums: list[int]):
    prefixArray = [1]
    suffixArray = [1]
    size = len(nums)

    for i in range(1,size):
        prefixArray.append(nums[i-1] * prefixArray[i-1])
    
    for i in range(1,size):
        suffixArray.append(nums[size-i] * suffixArray[i-1])

    i , j = 0, size - 1
    resultArray = []

    while i < size and j >=0 :
        resultArray.append(prefixArray[i] * suffixArray[j])
        i += 1
        j -= 1
    
    return resultArray


print(productExceptSelf([1,2,3,4]))


        