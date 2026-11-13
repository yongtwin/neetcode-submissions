class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i,num in enumerate(nums):
            current = target - num
            if current in seen:
                return[seen[current], i]
            seen[num]=i 
                    