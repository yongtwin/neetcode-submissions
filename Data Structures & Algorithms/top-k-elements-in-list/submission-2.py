class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        heap = []
        for countKey in counts.keys():
            heapq.heappush(heap, (counts[countKey], countKey))
            if (len(heap) > k):
                heapq.heappop(heap)

        res = []
        for index in range(k):
            res.append(heapq.heappop(heap)[1])
        return res