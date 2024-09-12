def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    positionSpeed = [[p, s] for p, s in zip(position, speed)]

    fleetStack = []
    for p, s in sorted(positionSpeed)[::-1]:
        reach = (target - p)/s
        fleetStack.append(reach)

        if len(fleetStack) > 1 and fleetStack[-1] <= fleetStack[-2]:
            fleetStack.pop()

    return len(fleetStack)

print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
        


        