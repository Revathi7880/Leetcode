using System;

public class Solution {
    public int MaxSubArray(int[] nums) {
        int maxSum = Int32.MinValue;
        int currentSum = 0;

        foreach(var n in nums)
        {
            currentSum += n;
            if (currentSum > maxSum) {
                maxSum = currentSum;
            } 
            if (currentSum < 0) {
                currentSum = 0;
            } 
        }
        return maxSum;
    }
}

var nums = new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
var solution = new Solution();
Console.WriteLine(solution.MaxSubArray(nums))


