from heapq import heappop, heappush, heapify
def topKFrequent(nums: list[int], k: int):
    freqDict = {}
    countHeap = []
    heapify(countHeap)
    resultList = []

    for n in nums:
        if n in freqDict:
            freqDict[n] += 1
        else:
            freqDict[n] = 1
    
    for num in freqDict:
        heappush(countHeap, [-1*freqDict[num], num])
    
    while k > 0:
        ele = heappop(countHeap)
        resultList.append(ele[1])
        k -= 1
    
    return resultList

print(topKFrequent([1,1,1,2,2,3], 2))

