class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        l, r = 0, 0
        chars_set = set()
        while r < len(s):
            while s[r] in chars_set:
                chars_set.remove(s[l])
                l += 1
            chars_set.add(s[r])
            longest_len = max(longest_len, len(chars_set))
            r += 1
        return longest_len