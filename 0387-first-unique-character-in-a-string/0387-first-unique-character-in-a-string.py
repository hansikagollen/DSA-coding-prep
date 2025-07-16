class Solution:
    def firstUniqChar(self, s: str) -> int:
        string=Counter(s)
        for i,char in enumerate(s):
            if string[char]==1:
                return i
        return -1
        