def twoSum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = len(numbers) - 1

    while i < j:
        addition = numbers[i] + numbers[j]
        if addition == target:
            return [i + 1, j + 1]
        elif addition > target:
            j -= 1
        else:
            i += 1

print(twoSum([2,7,11,15], 9))
            


        