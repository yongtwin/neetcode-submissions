class Solution:
    delimeter = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for text in strs:
            res += str(len(text)) + self.delimeter + text

        return res
            

    def decode(self, s: str) -> List[str]:
        startIndex = 0
        endIndex = 0
        
        res = []
        while endIndex < len(s):
            lengthOfText = 0

            if s[endIndex] != self.delimeter:
                endIndex += 1
            else:
                lengthOfText = int(s[startIndex:endIndex])
                startIndex = endIndex + 1
                endIndex = startIndex + lengthOfText

                res.append(s[startIndex:endIndex])

                startIndex = endIndex
        
        return res