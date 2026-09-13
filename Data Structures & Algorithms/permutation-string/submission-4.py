class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, 0
        s1_map = defaultdict(int)
        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)
        
        s2_map = defaultdict(int) # map of s1 len substr in s2
        for i in range(len(s1)):
            s2_map[s2[i]] = 1 + s2_map.get(s2[i], 0)
            r += 1
            
        while r < len(s2):
            if s1_map == s2_map:
                return True
            
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            s2_map[s2[r]] += 1

            l += 1
            r += 1
        
        if s1_map == s2_map:
            return True

        return False
