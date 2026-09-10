class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        minK = r

        while l <= r:
            m = (r + l) // 2
            totalTime = 0
            for i in range(len(piles)):
                totalTime += math.ceil(piles[i]/m)
            if totalTime <= h:
                minK = m
                r = m - 1
            elif totalTime > h:
                l = m + 1

        return minK
            