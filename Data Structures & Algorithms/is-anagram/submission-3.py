class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        charCountS = {}
        charCountT = {}

        for index in range(len(s)):
            charCountS[s[index]] = 1 + charCountS.get(s[index], 0)
            charCountT[t[index]] = 1 + charCountT.get(t[index], 0)
        
        return charCountS == charCountT