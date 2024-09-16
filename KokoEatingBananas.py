
import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    l = 1
    r = max(piles)
    minSpeed = r

    while l <= r:
        mid = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p/mid)
        if hours <= h:
            minSpeed = min(mid, minSpeed)
            r = mid - 1
        else:
            l = mid + 1
    return minSpeed

print(minEatingSpeed([30,11,23,4,20], 6))






        