class Solution:
    def longestConsecutive(self,nums):
        maxlen= 0
        nums_set = set(nums)

        for num in nums:
            if num-1 not in nums_set:
                curlen=1
                curnum=num
                while curnum+1 in nums_set:
                    curnum+=1
                    curlen+=1
                maxlen = max(maxlen,curlen)
        return maxlen

nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))
