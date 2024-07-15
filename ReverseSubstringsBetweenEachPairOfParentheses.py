def reverseParentheses(s):
    bracketStack = []
    letterStack =[]
    reverse = ""
    for i in range(len(s)):
        if s[i] == '(':
            bracketStack.append(len(letterStack))
        elif s[i] == ')':
            index = bracketStack.pop()
            letterStack[index:i] = reversed(letterStack[index:i])
        else:
            letterStack.append(s[i])
    return reverse.join(letterStack)

s = input("enter a string: ")
print(reverseParentheses(s))
         
        