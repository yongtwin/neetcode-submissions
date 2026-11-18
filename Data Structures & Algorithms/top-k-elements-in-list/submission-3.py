class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for index in range(len(nums)):
            counts[nums[index]] = 1 + counts.get(nums[index], 0)
        
        heap = []
        for key in counts.keys():
            heapq.heappush(heap, [counts[key], key])
            if (len(heap) > k):
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res