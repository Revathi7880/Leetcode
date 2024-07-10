def averageWaitingTime(customers):
    currentTime = 1
    finishTime = 0
    for customer in customers:
        if customer[0] > currentTime:
            currentTime = customer[0]
        currentTime += customer[1]
        finishTime = finishTime + (currentTime - customer[0])
    
    return float(finishTime) / len(customers)

customerCount = int(input("Enter Number of Customers: "))
customers = []
for i in range(customerCount):
    consoleInput = input("enter customer's arrival and food prep time: ")
    customer = [int(i) for i in consoleInput.split()]
    customers.append(customer)

print(averageWaitingTime(customers))



    