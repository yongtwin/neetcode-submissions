class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        for index in range(1, len(nums)):
            res[index] = res[index - 1] * nums[index - 1]
        
        postFix = 1
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= postFix
            postFix *= nums[index]
        return res