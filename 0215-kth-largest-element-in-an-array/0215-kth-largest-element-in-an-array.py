class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        count=0
        for num in nums:
            count+=1
            heapq.heappush(heap,num)
            if count>k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
        