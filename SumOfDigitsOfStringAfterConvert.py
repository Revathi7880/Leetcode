def getLucky(s, k):

        numberString = ""
        for alpha in s:
            numberString += '{}'.format((ord(alpha) - 96))
        
        number = int(numberString)

        for i in range(0, k):
            numberSum = 0
            while (number > 0):
                digit = number % 10
                numberSum += digit
                number = int(number / 10)
            number = numberSum
        
        return number


print(getLucky("zbax", 2))


        