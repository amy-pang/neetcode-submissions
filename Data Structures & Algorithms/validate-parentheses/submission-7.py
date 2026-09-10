class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                if c == ")":
                    if top != "(":
                        return False
                elif c == "}":
                    if top != "{":
                        return False
                else:
                    if top != "[":
                        return False
        if stack:
            return False
        return True