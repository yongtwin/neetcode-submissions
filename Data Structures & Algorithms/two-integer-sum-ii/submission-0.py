class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}

        for index, num in enumerate(numbers):
            cur = target - num

            if cur in map:
                return [map[cur] + 1, index + 1] 
            else:
                map[num] = index

        return [] 