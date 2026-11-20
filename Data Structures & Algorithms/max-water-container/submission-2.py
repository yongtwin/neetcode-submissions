class Solution:
    def maxArea(self, heights: List[int]) -> int:
        startIndex, endIndex = 0, len(heights) - 1
        res = 0

        switch = False
        while startIndex < endIndex:
            area = min(heights[startIndex], heights[endIndex]) * (endIndex - startIndex)
            res = max(res, area)
            
            if heights[startIndex] < heights[endIndex]:
                startIndex += 1
            else:
                endIndex -= 1
        
        return res