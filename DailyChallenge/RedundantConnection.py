def findRedundantConnection(edges):
    n = len(edges)
    rootList = [-1] * n

    for e in edges:
        ar = []
        for i in e:
            node = i - 1
            while rootList[node] != -1:
                node = rootList[node]
            ar.append(node)
        if ar[0] == ar[1]:
            return e
        else:
            rootList[ar[0]] = ar[1]

print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))