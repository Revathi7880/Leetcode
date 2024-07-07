def canJump(nums):
    far = 0
    for i in range(len(nums)):
        if i > far:
            return False
        far = max(far, i + nums[i])
    
    if far >= len(nums) - 1:
        return True
        
consoleInput = input("Enter jumps array: ")
nums = [int(n) for n in consoleInput.split()]
print(canJump(nums))
    