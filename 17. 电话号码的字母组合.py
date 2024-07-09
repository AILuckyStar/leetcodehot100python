class Solution:
    def __init__(self):
        self.phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    def backtracking(self,res,combination,digits):
        if len(digits)==0:
            res.append(combination)
            return
        for letter in self.phone[digits[0]]:
            self.backtracking(combination+letter,digits[1:])


    def letterCombinations(self,digits):
        if not digits:
            return []
        res=[]
        self.backtracking(res,'',digits)
        return res
