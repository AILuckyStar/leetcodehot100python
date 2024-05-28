from typing import List


class Solution:
    def twoSum(self,nums:List[int],target:int)-> List[int]:
        hashtable = dict()
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[num] = i
        return []

list1 = [2,7,11,15]
target1 = 9
sol  = Solution()
print(sol.twoSum(list1,target1))
