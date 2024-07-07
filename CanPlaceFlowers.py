def canPlaceFlowers(flowerbed, n):
    i = 0
    while i < len(flowerbed):
        if len(flowerbed) == 1 and flowerbed[i] == 0:
            n -= 1 
            i += 1
        elif flowerbed[i] == 1:
            i += 1
        elif i == 0:
            if flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
            i += 1
        elif i == len(flowerbed) - 1:
            if flowerbed[i - 1] == 0:
                n -= 1
                flowerbed[i] = 1
            i += 1
        else:
            if flowerbed[i -1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
            i += 1
                

    if n <= 0:
        return True
    else:
        return False

consoleInput1 = input("Enter flowerbed array: ")
flowerbed = [int(n) for n in consoleInput1.split()] 
n = int(input("Enter n value: "))

print(canPlaceFlowers(flowerbed, n))


    