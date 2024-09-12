def isValid(s: str) -> bool:
    paranthStack = []
    for paranth in s:
        if paranth == '(' or paranth =='{' or paranth == '[':
            paranthStack.append(paranth)
        else :
            if not paranthStack:
                return False
            ele = paranthStack.pop()
            if (paranth == ')' and ele != '(') or (paranth == '}' and ele != '{') or (paranth == ']' and ele != '['):
                return False
    if not paranthStack:
        return True
    return False

print(isValid('{((([{[}])))}'))


        