class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency ={}
        for num in nums:
            if num not in frequency:
                frequency[num]= frequency.get(num, 1)
            else:
                frequency[num] +=1
        result = []
        for num in sorted(frequency.items(), key = lambda x: x[1], reverse = True):
            if k!=0:
                result.append(num[0])
                k -=1
        return result