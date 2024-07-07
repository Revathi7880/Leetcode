def maxArea(height):
    i, j = 0, len(height) - 1
    maxArea = 0 

    while i < j:
        length = j - i
        bredth = height[i] if height[i] <= height[j] else height[j]
        area = length * bredth
        if area > maxArea:
            maxArea = area
        if height[i] <= height[j]:
            i += 1
        else :
            j -= 1
    
    return maxArea

consoleInput = input("Enter height array: ")
height = [int(n) for n in consoleInput.split()]
print(maxArea(height))