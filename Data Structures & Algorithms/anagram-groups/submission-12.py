class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            alphabet = [0] *26
            for c in string:
                alphabet[ord(c) - ord('a')] +=1
            # sorted_text = "".join(sorted(string))
            groups[tuple(alphabet)].append(string)

        return list(groups.values())