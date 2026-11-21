class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        startIndex, endIndex = 0, 1
        maxProfit = 0

        while endIndex < len(prices):
            if prices[startIndex] > prices[endIndex]:
                startIndex = endIndex
            else:
                maxProfit = max(maxProfit, prices[endIndex] - prices[startIndex])
            
            endIndex += 1

        return maxProfit