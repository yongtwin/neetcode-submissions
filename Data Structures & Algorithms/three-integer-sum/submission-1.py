class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, num in enumerate(nums):
            if num > 0:
                break
            
            if index > 0 and num == nums[index - 1]:
                continue
            
            startIndex, endIndex = index + 1, len(nums) - 1
            while startIndex < endIndex:
                sum = num + nums[startIndex] + nums[endIndex]
                if sum > 0:
                    endIndex -= 1
                elif sum < 0:
                    startIndex += 1
                else:
                    res.append([num, nums[startIndex], nums[endIndex]])
                    
                    startIndex += 1
                    endIndex -= 1

                    while nums[startIndex] == nums[startIndex - 1] and startIndex < endIndex:
                        startIndex += 1

        return res