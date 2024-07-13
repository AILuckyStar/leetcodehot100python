import random


class Solution:
    def quickFind(self,nums,k):
        pivot = random.choice(nums)
        big,equal,small=[],[],[]
        for num in nums:
            if num>pivot:
                big.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                small.append(num)
        if k<=len(big):
            return self.quickFind(big,k)
        elif k>len(big)+len(equal):
            return self.quickFind(small,k-(len(big)+len(equal)))
        else:
            return pivot
    def findKthLargest(self,nums,k):
        return self.quickFind(nums,k)
