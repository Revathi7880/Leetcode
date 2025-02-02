def check(self, nums) -> bool:
    rotationPoint = 0
    n = len(nums)
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            rotationPoint += 1
            if rotationPoint > 1:
                return False
    if rotationPoint > 0:
        if nums[n-1] > nums[0]:
            return False
    return True
                