class Solution:
    def maxProfit(self,prices):
        maxprofit,minprice=float('-inf'),float('inf')
        for price in prices:
            minprice=min(minprice,price)
            maxprofit=max(maxprofit,price-minprice)
        return maxprofit
