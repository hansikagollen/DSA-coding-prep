class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        minimum=nums[0]
        for i in range(1,len(nums)):
            minimum=min(minimum,nums[i])
            if nums[i]>minimum:
                ans=max(ans,nums[i]-minimum)
        return ans
        