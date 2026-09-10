class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combos = set()

        def dfs(i, subset, total):
            if total == target:
                tupleSubset = tuple(subset)
                if tupleSubset not in combos:
                    res.append(subset.copy())
                    combos.add(tupleSubset)
                return
            if i == len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])

            subset.pop()
            dfs(i + 1, subset, total)
        
        candidates.sort()
        dfs(0, [], 0)
        return res