class Solution:
    def isHappy(self, n: int) -> bool:
        slow=self.number(n)
        fast=self.number(self.number(n))

        while slow!=fast and fast!=1:
            slow=self.number(slow)
            fast=self.number(self.number(fast))
        return fast==1

    def number(self,num):
        count=0
        while num!=0:
            rem=num%10
            count=count+(rem**2)
            num=num//10
        return count        