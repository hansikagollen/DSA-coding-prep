class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=Counter(nums)
        for i in n.values():
            if i%2!=0:
                return False

        return True
        