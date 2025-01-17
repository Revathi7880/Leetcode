using System;

public class Solution {
    public bool DoesValidArrayExist(int[] derived) {
        int res = derived[0];
        foreach(int n in derived.Skip(1).ToArray()) {
            res = res ^ n;
        }
        if(res == 0) {
            return true;
        }
        else{
            return false;
        }
    }
}

var nums = new int[] {1,1,0};
var solution = new Solution();
Console.WriteLine(solution.DoesValidArrayExist(nums))