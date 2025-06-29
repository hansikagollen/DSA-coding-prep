class Solution:
    def isPalindrome(self,s):
        left = 0
        right = len(s) - 1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        def backtrack(idx):
            if idx==len(s):
                res.append(temp.copy())
                return 
            for i in range(idx,len(s)):
                if self.isPalindrome(s[idx:i+1]):
                    temp.append(s[idx:i+1])
                    backtrack(i+1)
                    temp.pop()
            return
        backtrack(0)
        return res