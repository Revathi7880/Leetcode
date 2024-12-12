import heapq
import math

def pickGifts(gifts, k: int) -> int:
    maxHeap = []
    sumGifts = 0
    for g in gifts:
        heapq.heappush(maxHeap, -g)
    for i in range(k):
        maxGift = -heapq.heappop(maxHeap)
        sqrtMaxHeap = math.floor(math.sqrt(maxGift))
        heapq.heappush(maxHeap, -sqrtMaxHeap)
    for i in range(len(maxHeap)):
        sumGifts += (-heapq.heappop(maxHeap))

    return sumGifts

print(pickGifts([1,1,1,1], 4))



    