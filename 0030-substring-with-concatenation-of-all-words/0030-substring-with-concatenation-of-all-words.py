class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_l=len(words[0])
        word_c=len(words)
        word_length=word_l*word_c
        if len(s)<word_length:
            return[]

        from collections import Counter
        word_counter=Counter(words)
        start=0
        res=[]

        for i in range(len(s)-word_length+1):
            window=s[i:i+word_length]
            word_length_counter=Counter()

            for j in range(0,word_length,word_l):
                word=window[j:j+word_l]
                word_length_counter[word]+=1

            if word_counter==word_length_counter:
                res.append(i)

        return res    

        
        