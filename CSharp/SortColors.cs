using System;

public class Solution {
    public int[] SortColors(int[] nums) {
        Dictionary<int, int> countDict = new Dictionary<int, int>{
            {0, 0},{1, 0},{2, 0}
        };
        foreach(var n in nums){
            countDict[n] += 1;
        }
        int initialIndex = 0;
        foreach(KeyValuePair<int, int> ele in countDict) {
            for(int i = initialIndex; i < initialIndex + ele.Value; i++){
                nums[i] = ele.Key;
            }
            initialIndex += ele.Value;
        }
        return nums;
    }
}

int[] nums = {2, 0, 2, 1, 1, 0};
var solution = new Solution();
int[] ans = solution.SortColors(nums);
Console.WriteLine("["+string.Join(",", ans)+"]")
