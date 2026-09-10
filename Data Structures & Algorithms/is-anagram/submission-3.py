class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        for c in s:
            if c in sChars:
                sChars[c] += 1
            else:
                sChars[c] = 1
        
        for c in t:
            if c not in sChars or sChars[c] == 0:
                return False
            sChars[c] -= 1
        
        return True if all(value == 0 for value in sChars.values()) else False