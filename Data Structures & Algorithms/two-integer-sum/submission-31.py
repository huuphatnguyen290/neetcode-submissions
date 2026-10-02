class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash ={}
        check=0
        for i, num in enumerate(nums):
            check = target -num
            if check not in hash:
                hash[num] = i
            else:
                return [hash[check], i]
