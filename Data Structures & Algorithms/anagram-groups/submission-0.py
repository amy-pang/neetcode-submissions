class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #initialize

        for s in strs:
            alphab = [0] * 26
            for c in s:
                alphab[ord(c) - ord('a')] += 1
            
            result[tuple(alphab)].append(s)
        
        return result.values()