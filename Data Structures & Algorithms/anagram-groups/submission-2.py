class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}

        for text in strs:
            sortedTextList = sorted(text)
            sortedText = "".join(sortedTextList)
            if groupMap.get(sortedText):
                groupMap[sortedText].append(text)
            else:
                groupMap[sortedText] = [text]
        return list(groupMap.values())