class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check ={}
        for i in range(len(nums)):
            goal = target- nums[i]
            if goal not in check:
                check[nums[i]] = i
            else:
                return [check[goal], i]
            