class Solution:
    def backtracking(self, res, ans, left, right, n):
        if len(ans) == 2 * n:
            res.append(ans)
            return
        if left < n:
            self.backtracking(res, ans + '(', left + 1, right, n)
        if right < left:
            self.backtracking(res, ans + ')', left, right + 1, n)

    def generateParenthesis(self, n):
        res = []
        self.backtracking(res, '', 0, 0, n)
        return res
