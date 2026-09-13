class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count of letters in t matters
        if len(s) < len(t):
            return ""
        
        l = 0
        t_map = defaultdict(int) # target map
        for letter in t:
            t_map[letter] = 1 + t_map.get(letter, 0)
        
        s_map = defaultdict(int)
        shortest_len, shortest_l, shortest_r = float('inf'), 0, 0
        have, need = 0, len(t_map) # num distinct letters

        for r in range(len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)

            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                have += 1
                
            while have == need:
                if r - l + 1 < shortest_len:
                    shortest_len = r - l + 1
                    shortest_l = l
                    shortest_r = r

                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                
                l += 1
           
        return s[shortest_l:shortest_r + 1] if shortest_len != float('inf') else ""