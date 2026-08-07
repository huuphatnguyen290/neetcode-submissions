class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = 1
        for n in nums:
            if n not in freq:
                freq[n]=count
            else:
                freq[n] +=1
        arr =[]
        
        for num, cnt in freq.items():
            arr.append([cnt, num])
        arr.sort(reverse= True)
        result = []

        i = 0
        while len(result) < k :
            result.append(arr[i][1])
            i+=1
        return result

