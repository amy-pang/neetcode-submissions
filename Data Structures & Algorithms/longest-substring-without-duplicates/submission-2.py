class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        hashset = set()
        l = 0
        for r, c in enumerate(s):
            while c in hashset:
                hashset.remove(s[l])
                l += 1 
            hashset.add(c)
            length = max(length, r - l + 1)
        return length