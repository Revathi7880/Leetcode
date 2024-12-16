import heapq

def getFinalState(nums, k: int, multiplier: int):
    minHeap = []
    n = len(nums)
    finalList = [0] * n
    for i in range(n):
        heapq.heappush(minHeap, [nums[i],i])
    for i in range(k):
        minEle = heapq.heappop(minHeap)
        heapq.heappush(minHeap,[minEle[0]*multiplier, minEle[1]])
    for ele, index in minHeap:
        finalList[index] = ele
    
    return finalList

print(getFinalState([2,1,3,5,6],5,2))
    