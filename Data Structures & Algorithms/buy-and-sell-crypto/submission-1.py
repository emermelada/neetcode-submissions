class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = prices[0]
        best = 0
        for i in range(1, len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            elif prices[i] - minValue > best:
                best = prices[i] - minValue 
        return best
