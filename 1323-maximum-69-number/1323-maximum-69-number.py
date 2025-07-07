class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        sum=0
        for i in range(len(digits)):
            if digits[i]==6:
                digits[i]=9
                break
        for i in digits:
            sum=sum*10+i
        return sum