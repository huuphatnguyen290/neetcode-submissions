class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency ={}
        for num in nums:
            frequency[num]= frequency.get(num, 0) + 1

        result = []
        # for num in sorted(frequency.items(), key = lambda x: x[1], reverse = True):
        #     if k!=0:
        #         result.append(num[0])
        #         k -=1  #O(nlog(n))

        bucket = [[] for _ in range(len(nums) + 1)]
        for key, freq in frequency.items():
            bucket[freq].append(key)
        result = []
        

        for num in reversed(bucket):
            for i in num:
                result.append(i)
                if len(result) == k:
                    return result
                
