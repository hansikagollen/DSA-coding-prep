class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word=[]
        count=0
        for i in words:
            word.append(sorted(i))  
        for i in word:
            if word.count(i) == 2:
                count=count+1
        return count//2
        