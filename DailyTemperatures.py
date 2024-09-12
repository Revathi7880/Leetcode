def dailyTemperatures(temperatures: list[int]) -> list[int]:
    tempStack = []
    length = len(temperatures)
    resList = [0] * length

    for i in range(0, length):

        while tempStack and tempStack[-1][0] < temperatures[i]:
            ele = tempStack.pop()
            resList[ele[1]] = i - ele[1]
            

        tempStack.append([temperatures[i], i])
        
    return resList
            

print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))