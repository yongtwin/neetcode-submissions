class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for text in strs:
            sorted_chars = sorted(text)
            key = "".join(sorted_chars)
            res[key].append(text);
        return list(res.values())