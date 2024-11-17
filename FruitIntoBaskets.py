def totalFruit(fruits):
    l, r, maxSum = 0, 0, 0
    baskets = {}
    while r < len(fruits):
        if fruits[r] in baskets:
            baskets[fruits[r]] += 1
        else: 
            baskets[fruits[r]] = 1

        while len(baskets) > 2:
            baskets[fruits[l]] -= 1
            if baskets[fruits[l]] == 0:
                baskets.pop(fruits[l])
            l += 1

        maxSum = max(maxSum, sum(baskets.values()))
        r += 1

    return maxSum

print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))


