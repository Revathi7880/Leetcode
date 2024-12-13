import heapq

def findScore(nums) -> int:
    minHeap = []
    markedNums = [False] * len(nums)
    for i in range(len(nums)):
        heapq.heappush(minHeap, ([nums[i], i]))
    score = 0
    while minHeap:
        MinElement, minIndex = heapq.heappop(minHeap)
        if not markedNums[minIndex]:
            score += MinElement
            markedNums[minIndex] = True
            if minIndex > 0:
                markedNums[minIndex - 1] = True
            if minIndex < len(nums) - 1:
                markedNums[minIndex + 1] = True
    return score

print(findScore([10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]))
    


    