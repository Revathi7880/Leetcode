def evalRPN(tokens: list[str]) -> int:
    numStack = []
    for t in tokens:
        if t != '*' and t != '+' and t != '-' and t != '/' :
            numStack.append(t)
        else :
            if not numStack:
                return 0
            ele2 = numStack.pop()
            ele1 = numStack.pop()
            res = eval(f"{ele1} {t} {ele2}")
            numStack.append(int(res))
    return int(numStack.pop())

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


