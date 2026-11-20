class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0

        numSet = set(nums)
        
        longestStreak = 1
        for num in numSet:
            tempLongestStreak = 1

            if num - 1 in numSet:
                continue
            else:
                tempNum = num + 1
                while tempNum in numSet:
                    tempLongestStreak += 1
                    tempNum += 1
            
            longestStreak = max(longestStreak, tempLongestStreak)
        
        return longestStreak