class Solution:
    def partitionLabels(self,s):
        endidx={}
        for i in range(len(s)):
            endidx[s[i]]=i
        start,end=0,0
        res=[]
        for i in range(len(s)):
            end=max(end,endidx[s[i]])
            if i==end:
                res.append(end-start+1)
                start=end+1
        return res
