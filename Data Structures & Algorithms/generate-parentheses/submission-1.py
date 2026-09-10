class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.addParenthesis(res, [], 0, 0, n)
        return res
            
    def addParenthesis(self, res, tmp, open, closed, n):
        if open == n and closed == n:
            res.append("".join(tmp))
            return 
        if open < n:
            tmp.append("(")
            self.addParenthesis(res, tmp, open + 1, closed, n)
            tmp.pop()
        if closed < open:
            tmp.append(")")
            self.addParenthesis(res, tmp, open, closed + 1, n)
            tmp.pop()