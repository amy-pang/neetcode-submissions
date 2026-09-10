class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxL = 0
        mostFreq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            mostFreq = max(mostFreq, count[s[r]])

            # number of chars that need to be replaced
            while (r - l + 1) - mostFreq > k:
                count[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
        
        return maxL
            