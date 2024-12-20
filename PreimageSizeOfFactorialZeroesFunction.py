def preimageSizeFZF(k: int) -> int:
    left = 0
    right = (k + 1) * 5

    while left <= right:
        mid = (left + right) // 2

        start = 5
        count = 0
        while mid // start:
            count += mid // start
            start *= 5
        
        if count == k:
            return 5
        elif count > k:
            right = mid - 1
        else:
            left = mid + 1
    
    return 0

print(preimageSizeFZF(200))

    