class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0
        
        for char in charSet:
            count = startIndex = 0

            for endIndex in range(len(s)):
                if s[endIndex] == char:
                    count += 1
                
                while (endIndex - startIndex + 1) - count > k:
                    if s[startIndex] == char:
                        count -= 1
                    startIndex += 1
                
                res = max(res, endIndex - startIndex + 1)
        
        return res