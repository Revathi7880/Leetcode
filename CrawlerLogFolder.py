def minOperations(logs):
    stack= []
    for operation in logs:
        if operation == "../":
            if stack:
                stack.pop()
        elif operation[0] != ".":
            stack.append(operation)

    return len(stack)

consoleInput = input("Enter logs: ")
logs = [i for i in consoleInput.split()]

print(minOperations(logs))