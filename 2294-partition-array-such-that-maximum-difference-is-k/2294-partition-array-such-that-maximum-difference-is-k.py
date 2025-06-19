class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums=sorted(list(set(nums)))
        ans=1
        minimum=nums[0]

        for nums in nums:
            if nums-minimum>k:
                ans+=1
                minimum=nums

        return ans

        