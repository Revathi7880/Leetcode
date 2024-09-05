def chalkReplacer(chalk, k):
    numbersSum = sum(chalk)
    remaining = k % numbersSum
    if remaining == 0 :
        return 0
    else :
        for i in range(0, len(chalk)):
            if remaining - chalk[i] < 0:
                return i
            remaining -= chalk[i]

print(chalkReplacer([22,86,96,35,62,69,56,33,95,10,38,53,33,90,29,68,85,58,11,49,81,18,32,96,40,75,49,26,60,71,15,94,31,99,12,81,10,19,7,73,35,56,100,15,37,89,58,17,55,62,4,30,68,68,89,62,39,35,16,18,63,73,100,22,46,58,80,77,23,5,52,96,98,21,33,86,81,71,69,72,71,58,17,85,70,22,84,94,75,51,60,81,12,22,13,33,53,58], 134221332))
        

                



        