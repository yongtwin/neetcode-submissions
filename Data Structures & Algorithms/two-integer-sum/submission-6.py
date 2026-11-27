class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            current = target - nums[i]
            if current in map:
                return [map[current], i]
            
            map[nums[i]] = i
            
        return []