class Solution:
    def generate(self,numRows):
        res=[[1]]
        for i in range(1,numRows):
            ans=[0]*(i+1)
            ans[0]=1
            ans[i]=1
            for j in range(1,i):
                ans[j]=res[i-1][j-1]+res[i-1][j]
            res.append(ans)
        return res
