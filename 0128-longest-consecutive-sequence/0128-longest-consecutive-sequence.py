class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        c=1
        r=1
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            if nums[i+1]==nums[i]+1:
                c+=1
            else:
                r=max(r,c)
                c=1
        return max(r,c)