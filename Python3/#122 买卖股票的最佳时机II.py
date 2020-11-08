# 考虑可以当天买入当天卖出
# 执行用时：76ms，击败80.66%
# 内存消耗：14.7MB，击败49.71%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = 0
        for i in range(len(prices)-1):
            add = prices[i+1] - prices[i]
            if add >0:
                n+=add
        return n
