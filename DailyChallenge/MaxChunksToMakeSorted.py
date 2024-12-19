def maxChunksToSorted(arr) -> int:
    maxSeen = 0
    chunkCount = 0
    for ind, num in enumerate(arr):
        maxSeen = max(maxSeen, num)
        if maxSeen == ind:
            chunkCount += 1
    return chunkCount

print(maxChunksToSorted([1,4,3,6,0,7,8,2,5]))