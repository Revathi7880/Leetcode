def numWaterBottles(numBottles, numExchange):
    drink = numBottles
    num = numBottles 
    while num >= numExchange:
        exchange = num // numExchange
        drink += exchange
        rem = num - (exchange * numExchange)
        num = exchange + rem

    return drink 

numBottles = int(input('Enter the number of bottles: '))
numExchange = int(input('The exchange number: '))

print(numWaterBottles(numBottles, numExchange))


    