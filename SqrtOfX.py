def mySqrt(x: int) -> int:
    if x == 0 or x ==1:
        return x
    left = 0
    right = x
    sqrt = 0

    while left <= right :
        mid = (left + right) // 2
        if mid == x/mid:
            return mid
        elif mid < x/mid:
            sqrt = mid
            left = mid + 1
        else:
            right = mid - 1
    return sqrt

print(mySqrt(8))
    