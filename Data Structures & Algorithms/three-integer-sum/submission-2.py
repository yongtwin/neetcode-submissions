class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and num == nums[i - 1]:
                continue

            startIndex, endIndex = i + 1, len(nums) - 1
            while startIndex < endIndex:
                ttl = num + nums[startIndex] + nums[endIndex]
                if ttl > 0:
                    endIndex -= 1
                elif ttl < 0:
                    startIndex += 1
                else:
                    res.append([num, nums[startIndex], nums[endIndex]])
                    startIndex += 1
                    endIndex -= 1
                    while nums[startIndex] == nums[startIndex - 1] and startIndex < endIndex:
                        startIndex += 1

        return res