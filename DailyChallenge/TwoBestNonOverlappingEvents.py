def maxTwoEvents(events):
    sortedEvents = sorted(events, key = lambda e: e[0])
    n = len(events)
    suffixMax = [0] * n
    suffixMax[n-1] = sortedEvents[n-1][2]
    for i in range(n-2, -1, -1):
        suffixMax[i] = max(sortedEvents[i][2], suffixMax[i+1])
    
    maxValue = 0

    for i in range(n):
        left = i + 1
        right = n - 1
        firstNonOverlapIndex = -1
        sum = sortedEvents[i][2]
        while left <= right:
            mid = (left + right) // 2
            if sortedEvents[mid][0] > sortedEvents[i][1]:
                firstNonOverlapIndex = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if firstNonOverlapIndex != -1:
            sum += suffixMax[firstNonOverlapIndex]
        
        maxValue = max(sum, maxValue)
        
    return maxValue

print(maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))