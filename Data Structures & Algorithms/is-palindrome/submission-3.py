class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredStr = []
        for i in range(len(s)):
            if s[i].isalnum():
                filteredStr.append(s[i].lower())

        startIndex, endIndex = 0, len(filteredStr) - 1
        while startIndex < endIndex:
            if filteredStr[startIndex] != filteredStr[endIndex]:
                return False
            else:
                startIndex += 1
                endIndex -= 1

        return True