def bestClosingTime(customers: str) -> int:
    n = len(customers)
    countN = [0]
    countY = [0]*(n+1)
    countY[-1] = 0
    minPenalityIndex = 0
    minPenality = float('inf')
    

    for i in range(n):
        if customers[i] == 'N':
            countN.append(countN[i] + 1)
        else:
            countN.append(countN[i] + 0)

    for i in range(n-1,-1,-1):
        if customers[i] == 'Y':
            countY[i] = countY[i+1] + 1
        else:
            countY[i] = countY[i+1] + 0
    
    for i in range(len(countY)):
        if countY[i] + countN[i] < minPenality:
            minPenalityIndex = i
            minPenality = countY[i] + countN[i]
    return minPenalityIndex

print(bestClosingTime("NYYYNNNYNN"))
