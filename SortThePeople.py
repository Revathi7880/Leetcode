def sortPeople(names, heights):
    personDict = {}
    resultList = []
    for i in range(len(names)):
        personDict[heights[i]] = names[i]

    sortedHeights = sorted(heights, reverse=True)

    for height in sortedHeights:
        resultList.append(personDict[height])
    
    return resultList

n = int(input("Enter the size: "))
names = []
heights = []
for i in range(n):
    name = input("Enter Name: ")
    names.append(name)

for i in range(n):
    height = input("Enter heights: ")
    heights.append(int(height))

print(sortPeople(names, heights))



            





        
        