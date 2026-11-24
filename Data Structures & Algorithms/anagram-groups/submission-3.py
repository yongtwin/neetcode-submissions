class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for text in strs:
            sortedArr = sorted(text)
            sortedText = "".join(sortedArr)
            res[sortedText].append(text)

        return list(res.values())