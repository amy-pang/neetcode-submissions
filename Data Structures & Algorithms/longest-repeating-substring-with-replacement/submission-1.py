class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {} # char, int
        l = 0
        maxf = 0
        for r, c in enumerate(s):
            hashmap[c] = hashmap.get(c, 0) + 1
            maxf = max(maxf, hashmap[c])

            if (r - l + 1) - maxf > k:
                hashmap[s[l]] -= 1
                l += 1
                
        return r - l + 1