class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num]= frequency.get(num,0) +1
        
        # Create a storage with index represent for frequency
        storage = []
        for _ in range(len(nums) +1):
            storage.append([])
        
        for val, freq in frequency.items():
            storage[freq].append(val)

        result = []
        for num in storage[::-1]:
            # In case there are more than 1 value sharing the same frequency, so 1 index could get 2 values.
            if k!= 0:
                for val in num:
                    result.append(val)
                    k-=1
            else:
                return result
        return result


