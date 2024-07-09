def findTheWinner(n, k):
    friendQueue = []

    for i in range(1,n+1):
        friendQueue.append(i)
    while len(friendQueue) > 1:
        friendQueue = Eliminate(friendQueue, k)
    return friendQueue[0]


def Eliminate(friendQueue, k):
    print("in eliminate", friendQueue)
    for i in range(0, k):
        poppedElement = friendQueue.pop(0)
        friendQueue.append(poppedElement)
    friendQueue.pop(len(friendQueue) - 1)


    return friendQueue

n = int(input('Enter the number of friends: '))
k = int(input('The turn number: '))

print(findTheWinner(n, k))
    