class Solution:
    def majorityElement(self,nums):
        vote=0
        for num in nums:
            if vote==0:
                x=num
            if num==x:
                vote+=1
            else:
                vote-=1
        return x
