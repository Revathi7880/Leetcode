def finalPrices(prices):
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break
    return prices

print(finalPrices([8,4,6,2,3]))
    

        