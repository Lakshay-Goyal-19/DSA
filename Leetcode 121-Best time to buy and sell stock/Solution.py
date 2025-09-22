class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprofit=0
        price=prices[0]
        for i in range(1,len(prices)):
            if(price>prices[i]):
                price=prices[i]
            else:
                profit=prices[i]-price
                minprofit=max(minprofit,profit)
        return minprofit
        