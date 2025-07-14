class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_count=0
        max_len=0
        dic={}

        for right in range(len(s)):
            dic[s[right]]=dic.get(s[right],0)+1
            max_count=max(dic.values())
            windo_len=right-left+1

            if windo_len-max_count>k:
                dic[s[left]]-=1
                left+=1

            max_len=max(max_len,right-left+1)
        print(max_len)
        return max_len
        