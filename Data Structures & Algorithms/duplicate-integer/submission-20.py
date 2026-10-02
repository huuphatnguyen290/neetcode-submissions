class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash ={}
        for i, num in enumerate(nums):
            if num not in hash:
                hash[num] = i
            else:
                return True 

        return False