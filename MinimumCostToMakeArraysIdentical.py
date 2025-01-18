def minCost(arr, brr, k: int) -> int:
    if arr == brr:
        return 0
    n = len(arr)
    sortedArr = sorted(arr)
    sortedBrr = sorted(brr)
    totalCost = k
    totalCostW = 0

    for i in range(n):
        totalCost+= abs(sortedArr[i] - sortedBrr[i])
        totalCostW += abs(arr[i] - brr[i])

    return min(totalCost, totalCostW)

print(minCost([-7,9,5],[7,-2,-5],2))