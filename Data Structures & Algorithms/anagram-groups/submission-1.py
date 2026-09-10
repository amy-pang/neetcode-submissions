class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for c in s:
                ascii = ord(c) - ord('a')
                letters[ascii] += 1
            anagrams[tuple(letters)].append(s)

        result = []
        for words in anagrams.values():
            result.append(words)
        
        return result