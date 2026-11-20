class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        longestStreak = 0
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