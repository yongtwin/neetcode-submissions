public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int lengthOfNums = nums.Length;
        int[] res = new int[lengthOfNums];
        Array.Fill(res, 1);

        for (int i = 1; i < lengthOfNums; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }

        int postFix = 1;
        for (int i = lengthOfNums - 1; i >= 0; i--){
            res[i] *= postFix;
            postFix *= nums[i];
        }

        return res;
    }
}
