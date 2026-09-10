class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = -1
        while l <= r:
            temp_k = (r + l) // 2
            time = 0
            for p in piles:
                time += math.ceil(float(p) / temp_k)
            
            if time <= h:
                r = temp_k - 1
                k = temp_k
            else:
                l = temp_k + 1
        return k
        