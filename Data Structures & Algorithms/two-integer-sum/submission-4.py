class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffIndexHash = {}

        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in diffIndexHash:
                return [diffIndexHash.get(diff, 1), index]
            else:
                diffIndexHash[nums[index]] = index

        return []