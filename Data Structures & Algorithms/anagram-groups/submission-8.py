class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_list = defaultdict(list)
        for string in strs:
            sorted_text = "".join(sorted(string))
            if sorted_text not in hash_list:
                hash_list[sorted_text].append(string)
            else:
                hash_list[sorted_text].append(string)
        return list(hash_list.values())