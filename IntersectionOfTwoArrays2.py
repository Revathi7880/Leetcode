def intersect(nums1, nums2):
    sortedNums1 = sorted(nums1)
    sortedNums2 = sorted(nums2)
    intersectNums = []

    i, j = 0, 0

    while i < len(sortedNums1) and j < len(sortedNums2):
        if sortedNums1[i] == sortedNums2[j]:
            intersectNums.append(sortedNums1[i])
            i += 1
            j += 1
        elif sortedNums1[i] < sortedNums2[j]:
            i += 1
        else:
            j += 1

    return intersectNums

consoleInput1 = input("Enter array 1: ")
consoleInput2 = input("Enter array 2: ")
nums1 = [int(n) for n in consoleInput1.split()]
nums2 = [int(n) for n in consoleInput2.split()]

print(intersect(nums1, nums2))

                        



