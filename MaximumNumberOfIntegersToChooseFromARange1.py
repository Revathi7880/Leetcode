def maxCount(banned, n: int, maxSum: int) -> int:
    count = 0
    intSum = 0
    for i in range(1, n+1):
        if intSum + i > maxSum:
            return count
        if i not in banned:
            count += 1
            intSum += i
    return count

print(maxCount([1,6,5], 5, 6))
        