def largestRectangleArea(heights: list[int]) -> int:
    maxArea = 0
    heightStack = []

    for i in range(0, len(heights)):
        start = i

        while heightStack and heightStack[-1][0] > heights[i]:
            ele = heightStack.pop()
            area = ele[0] * (i - ele[1])
            maxArea = max(maxArea, area)
            start = ele[1]
        heightStack.append([heights[i], start])

    for ele in heightStack:
        area = ele[0] * (len(heights) - ele[1])
        maxArea = max(area, maxArea)
    
    return maxArea

print(largestRectangleArea([2,1,5,6,2,3]))


        