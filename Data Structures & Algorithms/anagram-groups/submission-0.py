class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            sorted_text= "".join(sorted(i))
            if sorted_text not in result:
                result[sorted_text] = [i]
            else:
                result[sorted_text].append(i)
        return list(result.values())
