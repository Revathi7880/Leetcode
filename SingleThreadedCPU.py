from heapq import heappush, heappop, heapify

def getOrder(tasks: list[list[int]]) -> list[int]:
    processQueue = []
    start = 0
    order = []

    for i in range(len(tasks)):
        tasks[i].append(i)

    tasks = sorted(tasks)
    time = tasks[0][0]

    while len(order) != len(tasks):
        while start < len(tasks) and tasks[start][0] <= time:
            heappush(processQueue,[tasks[start][1], tasks[start][2], tasks[start][0]])
            start += 1

        if processQueue:
            task = heappop(processQueue)
            order.append(task[1])
            isIdle = False
            time += task[0]
        else: 
            time = tasks[start][0]

    return order


print(getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))


    