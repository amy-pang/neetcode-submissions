class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        TotalLetters = 26
        anagrams = {} # ascii count, str
        for s in strs:
            asciiRep = [0] * TotalLetters
            for c in s:
                asciiRep[ord(c) - ord('a')] += 1

            key = tuple(asciiRep)
            if anagrams.get(key, 0) != 0:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        
        return list(anagrams.values())