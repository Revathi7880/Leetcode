def myAtoi(s):
        result = ''
        sign = ''
        for i in s:
            if i == "+" or i == "-":
                if not sign and not result :
                    sign = i
                else:
                    if result:
                        result = sign + result
                        num = int(result)
                        if num < (-2 ** 31):
                            return -2 ** 31
                        elif num > (2 ** 31) - 1:
                            return 2 ** 31 - 1
                        else:
                            return num
                    else:
                        return 0
            elif i.isnumeric():
                result = result + i
            elif i == " " and not result and not sign:
                result = result
            else:
                if result:
                    result = sign + result
                    num = int(result)
                    if num < (-2 ** 31):
                        return -2 ** 31
                    elif num > (2 ** 31) - 1:
                        return 2 ** 31 - 1
                    else:
                        return num
                else:
                    return 0

        if result:
            result = sign + result
            num = int(result)
            if num < (-2 ** 31):
                return -2 ** 31
            elif num > (2 ** 31) - 1:
                return 2 ** 31 - 1
            else:
                return num
        else:
            return 0
        
s = input("Enter a string: ")
print(myAtoi(s))
        




        