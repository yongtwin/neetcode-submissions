class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        startIndex = 0
        maxLength = 0

        for index in range(len(s)):
            while s[index] in charSet:
                charSet.remove(s[startIndex])
                startIndex += 1
            
            charSet.add(s[index])
            maxLength = max(maxLength, index - startIndex + 1)

        return maxLength