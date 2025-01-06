def minOperations(boxes: str):
    n = len(boxes)
    prefixSum = [0]
    suffixSum = [0]*n
    suffixSum[n-1] = 0
    result = []
    prefixBallCount = 1 if boxes[0] == "1" else 0
    suffixBallCount = 1 if boxes[n-1] == "1" else 0
    
    for i in range(1,n):
        prefixSum.append(prefixSum[i-1] + prefixBallCount)
        if boxes[i] == "1":
            prefixBallCount += 1

        suffixSum[n-1-i] = suffixSum[n-i] + suffixBallCount
        if boxes[n-1-i] == "1":
            suffixBallCount += 1
    
    for i in range(n):
        result.append(prefixSum[i] + suffixSum[i])
    return result

print(minOperations("001011"))

        



    
    
