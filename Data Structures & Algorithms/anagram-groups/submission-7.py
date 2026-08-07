class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for w in strs:
            binary = [0]*26
            for c in w:
                binary[ord(c) - ord('a')] +=1
            result[tuple(binary)].append(w)
            
        return list(result.values())