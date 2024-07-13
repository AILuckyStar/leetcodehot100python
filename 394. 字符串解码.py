class Solution:
    def decodeString(self,s):
        stk,res,num=[],"",0
        for c in s:
            if c.isalpha():
                res+=c
            elif c.isdigit():
                num=num*10+int(c)
            elif c=='[':
                stk.append([num,res])
                num,res=0,""
            elif c==']':
                curnum,lastres=stk.pop()
                res=lastres+curnum*res
        return res
