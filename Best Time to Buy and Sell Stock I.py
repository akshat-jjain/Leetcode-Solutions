class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=prices[0]
        maxprofit=0
        for x in range(1,len(prices)):
            p=prices[x]-b
            if p>maxprofit:
                maxprofit=p
            if b>prices[x]:
                b=prices[x]
        return maxprofit
