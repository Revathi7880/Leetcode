def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, k = m-1, n-1, m+n-1

    while i > -1 and j > -1 and k > -1:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j > -1:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
    return nums1
        
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))