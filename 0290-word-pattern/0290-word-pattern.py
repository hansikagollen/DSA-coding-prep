class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split=s.split()
        if len(pattern)!=len(split):
            return False
        p_s={}
        s_p={}    
        for i,word in zip(pattern,split):
            if i in  p_s:
                if p_s[i]!=word:
                    return False
            else:
                if word in s_p:
                    return False
                p_s[i]=word
                s_p[word]=i
        return True                                