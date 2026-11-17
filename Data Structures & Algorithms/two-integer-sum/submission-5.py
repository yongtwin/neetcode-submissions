class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffIndexHash = {}

        for index in range(len(nums)):
            currentVal = target - nums[index]

            if currentVal in diffIndexHash:
                return [diffIndexHash[currentVal], index]
            else:
                diffIndexHash[nums[index]] = index
        
        return []