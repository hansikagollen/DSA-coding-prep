class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        n=len(words)
        counter=Counter()
        wordslen=[]
        odd,even=0,0
        for w in words:
            wordslen.append(len(w))
            for c in w:
                counter[c]+=1
        for c in counter:
            even+=counter[c]//2
            odd+=counter[c]%2
        print("even,odd",even,odd)
        wordslen.sort()
        res=0
        for l in wordslen:
            if even>=l//2:
                even-=l//2
                if odd>=l%2:
                    odd-=l%2
                    res+=1
                elif even>0:
                    even-=1
                    odd+=1
                    res+=1
                else:
                    even+=l//2
        return res

        