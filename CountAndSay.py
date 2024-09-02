def countAndSay(n):
        if n == 1:
            return "1"
        
        rle = countAndSay(n - 1)
        result = ""
        i = 0
        count = 1
        rle += "0"
        while i < len(rle) - 1:
            if rle[i] == rle[i + 1]:
                count += 1
            else:
                result += '{}{}'.format(count, rle[i])
                count = 1
            i += 1
        return result
        
print(countAndSay(100))
        


        
        