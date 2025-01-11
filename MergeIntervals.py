def merge(intervals):
    sortedIntervals = sorted(intervals, key = lambda x: (x[0],x[1]))
    result = []
    n = len(intervals)
    temp = sortedIntervals[0]

    for i in range(1, n):
        if sortedIntervals[i][0] <= temp[1]:
            temp[1] = max(sortedIntervals[i][1], temp[1])
        else:
            result.append(temp)
            temp = sortedIntervals[i]
    result.append(temp)
    return result

print(merge([[1,3], [2,6] ,[8,10] ,[8,9], [9,11],[15,18], [2,4] ,[16,17]]))
            


    