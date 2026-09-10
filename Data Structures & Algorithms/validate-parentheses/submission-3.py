class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}": "{", ")": "(", "]": "["}
        stack = []
        for elt in s:
            if elt not in hashmap:
                stack.append(elt)
                continue
            if not stack or hashmap[elt] != stack[-1]:
                return False
            else:
                stack.pop()
        
        return not stack
            
            