import math
def minimumSize(nums, maxOperations: int) -> int:
    def penalityCheck(penality, numsList, maxOps):
        ops = 0
        for i in numsList:
            if i > penality:
                ops += math.ceil((i - penality)/penality)
        if ops <= maxOps:
            return True
        else: 
            return False


    left = 1
    right = max(nums)
    minPenality = float('inf')

    while left <= right:
        mid = (left + right) // 2
        penalityPossible = penalityCheck(mid, nums, maxOperations)
        if penalityPossible:
            minPenality = min(minPenality, mid)
            right = mid - 1
        else:
            left = mid + 1
    return minPenality

print(minimumSize([7,17], 2))



    