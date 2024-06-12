from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i = 0
        while (i < len(prices)): 
            minPrice = prices[i]
            maxPrice = prices[i]
            i += 1
            for j in range(i, len(prices)):
                if (prices[j] < minPrice):
                    break
                if (prices[j] > maxPrice):
                    maxPrice = prices[j]
                i+=1
            if(maxPrice - minPrice > maxProfit):
                maxProfit = maxPrice - minPrice
                
        return maxProfit

solution = Solution()
print("Run 1:")
print(f'Profit:{solution.maxProfit([7,1,5,3,6,4])}') # 5
print("Run 2:")
print(f'Profit:{solution.maxProfit([7,6,4,3,1])}') # 0
print("Run 3:") 
print(f'Profit:{solution.maxProfit([2,4,1])}') # 2