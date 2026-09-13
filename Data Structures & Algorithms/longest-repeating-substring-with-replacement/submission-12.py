class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_str = 0
        l, r = 0, 0
        window_size, max_freq = 0, 0
        count = defaultdict(int)    # count of char freqs of curr window

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            window_size += 1
            if window_size - max_freq > k:
                count[s[l]] -= 1
                l += 1
                window_size -= 1
            longest_str = max(longest_str, window_size)
            r += 1
            
        return longest_str
