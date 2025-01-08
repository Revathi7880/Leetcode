def maxProfit(prices) -> int:
    n = len(prices)
    suffixMax= [0] * n
    suffixMax[n-1] = prices[n-1]

    for i in range(n-2,-1,-1):
        suffixMax[i] = max(suffixMax[i+1],prices[i])
    
    maxProfit = 0
    for i in range(n-1):
        maxProfit = max(maxProfit, suffixMax[i+1] - prices[i])
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))


    