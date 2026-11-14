class Solution:
    delimeter = "#"

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for text in strs:
            lengthOfText = len(text)
            encodeStr = encodeStr + str(lengthOfText) + self.delimeter + text
        return encodeStr

    def decode(self, s: str) -> List[str]:
        strlist = []
        startIndex = 0
        while startIndex < len(s):
            endIndex = startIndex
            while s[endIndex] != self.delimeter:
                endIndex += 1
            lengthOfText = int(s[startIndex:endIndex])
            startIndex = endIndex + 1
            endIndex = startIndex + lengthOfText
            strlist.append(s[startIndex:endIndex])
            startIndex = endIndex
        return strlist
