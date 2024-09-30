def maxIceCream(costs: list[int], coins: int) -> int:
    iceCreamCount = 0
    sortedCosts = sorted(costs)
    totalCoins = coins
    i = 0
    while totalCoins > 0 and i < len(sortedCosts):
        if sortedCosts[i] <= totalCoins:
            iceCreamCount += 1
            totalCoins -= sortedCosts[i]
            i += 1
        else: 
            break
    return iceCreamCount

print(maxIceCream([1,6,3,1,2,5], 20))
    