def countOfAtoms(formula):
    indexStack = []
    countList = []
    name = ''
    num = ''
    i = 0
    
    while i < len(formula):
        if formula[i].isupper():
            if name != '':
                if num == '':
                    countList.append([name, 1])
                else:
                    countList.append([name, int(num)])
                name = ''
                num = ''
            name = name + formula[i]
            i = i + 1
        
        elif formula[i].islower():
            name = name + formula[i]
            i = i + 1

        elif formula[i].isnumeric():
            num = num + formula[i]
            i = i + 1

        elif formula[i] == '(':
            if name != '':
                if num == '':
                    countList.append([name, 1])
                else:
                    countList.append([name, int(num)])
                name = ''
                num = ''
            indexStack.append(len(countList))
            i = i + 1

        else:
            if name != '':
                if num == '':
                    countList.append([name, 1])
                else:
                    countList.append([name, int(num)])
                name = ''
                num = ''

            index = indexStack.pop()
            mulNum = ''
            j = i + 1
            while j < len(formula) and formula[j].isnumeric():
                mulNum = mulNum + formula[j]
                j = j + 1
            if mulNum != '':
                for k in countList[index: ]:
                    k[1] = k[1]*int(mulNum)
            i = j 

    if name != '':
        if num == '':
            countList.append([name, 1])
        else:
            countList.append([name, int(num)])
    
    countDict = {}
    for compound, count in countList:
        if compound in countDict:
            countDict[compound] += count
        else:
            countDict[compound] = count
    
    countList = sorted(countDict.items())
    atomCount = ''
    for i in countList:
        atomCount = atomCount + i[0] 
        if i[1] > 1:
            atomCount = atomCount + str(i[1])
            
    return atomCount

formula = input("Enter a formula: ")
print(countOfAtoms(formula))




                    

        
            



    