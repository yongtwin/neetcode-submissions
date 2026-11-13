class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for text in strs:
            sorted_chars = sorted(text)
            key = "".join(sorted_chars)
            if (map.get(key, 0)):
                map[key].append(text)
            else:
                map[key] = [text]
        return list(map.values())