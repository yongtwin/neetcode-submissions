class Solution:
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        resStr = ''
        for text in strs:
            resStr += str(len(text)) + self.delimiter + text
        return resStr

    def decode(self, s: str) -> List[str]:
        startIndexSubStr, endIndexSubStr = 0, 0

        res = []
        while endIndexSubStr < len(s):
            lengthOfText = 0
            if s[endIndexSubStr] != self.delimiter:
                endIndexSubStr += 1
            else:
                lengthOfText = s[startIndexSubStr:endIndexSubStr]
                startIndexSubStr = endIndexSubStr + 1
                endIndexSubStr = startIndexSubStr + int(lengthOfText)
                res.append(s[startIndexSubStr:endIndexSubStr])
                startIndexSubStr = endIndexSubStr
        return res
