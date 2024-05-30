import collections


class Solution:
    def minWindow(self,s,t):
        ans_left = -1
        ans_right = len(s)
        left=0
        counts = collections.Counter()
        countt = collections.Counter(t)
        for right,c in enumerate(s):
            counts[c] +=1
            while counts>=countt:
                if right-left < ans_right-ans_left:
                    ans_left,ans_right=left,right
                counts[s[left]]-=1
                left+=1
        return "" if ans_left==-1 else s[ans_left:ans_right+1]
s = "ADOBECODEBANC"
t = "ABC"
so = Solution()
print(so.minWindow(s,t))
