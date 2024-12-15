import heapq

def maxAverageRatio(classes, extraStudents: int) -> float:
        averageSum = 0
        averageList = []
        n = len(classes)

        for i, j in classes:
            averageSum += i/j
            averageList.append(((i - j)/(j*(j+1)), i, j))
        
        heapq.heapify(averageList)

        for i in range(extraStudents):
            avg, i, j = averageList[0]
            if avg == 0:
                break
            averageSum -= avg
            avg2 = (i - j)/((j + 1.0) * (j + 2.0))
            heapq.heapreplace(averageList, (avg2, i + 1, j + 1))
        return averageSum/ n

print(maxAverageRatio([[1,2],[3,5],[2,2]], 2))