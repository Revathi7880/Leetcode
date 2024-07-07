def findContentChildren(g, s):
    greedSorted = sorted(g)
    sizeSorted = sorted(s)
    content = 0
    i, j = 0, 0
    while i < len(greedSorted) and j < len(sizeSorted):
        if sizeSorted[j] >= greedSorted[i]:
            content += 1
            i += 1
            j += 1
        elif greedSorted[i] > sizeSorted[j]:
            j += 1
    return content

consoleInput1 = input("Enter greed array: ")
g = [int(n) for n in consoleInput1.split()]
consoleInput2 = input("Enter size array: ")
s = [int(n) for n in consoleInput2.split()]

print(findContentChildren(s, g))