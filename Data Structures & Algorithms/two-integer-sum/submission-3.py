class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            currentVal = target - num;

            if currentVal in map:
                return [map.get(currentVal, 1), i]
            else:
                map[num] = i

        return []