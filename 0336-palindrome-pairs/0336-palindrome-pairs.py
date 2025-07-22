class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        #Bruteforce
        # ans = []
        # def isPalindrome(s):
        #     return s == s[::-1]
        # for i,word1 in enumerate(words):
        #     for j in range(i+1,len(words)):
        #         if isPalindrome(word1+words[j]):
        #             ans.append([i,j])
        #         if isPalindrome(words[j]+word1):
        #             ans.append([j,i])
        # return ans
        #Store reverse words in map
        #if exact reverse is found, add them
        #if there is "" and already palindrome then add both cases
        #iterate through the word and if first part's reverse is found and rest is already palindrome add it
        #also check if second part's reverse is there and first part is already palindrome add accordingly
        dict = {}
        #Store all reversed word and the indexes
        for i,word in enumerate(words):
            dict[word[::-1]] = i
        ans = []
        for i,word in enumerate(words):
            #if the reverse is in map and its not the same index, add map value as a suffix
            if word in dict and dict[word] != i:
                ans.append([i, dict[word]])

            #if empty string is found, it can be combined to any already exisitng palindromes, add both as prefix and suffix
            if word != "" and "" in dict and word == word[::-1]:
                ans.append([dict[""],i])
                ans.append([i,dict[""]])

            #Slice the word in 2 parts for each index
            for j in range(len(word)):
                #Case 1: First part is in map, 2nd part is already palindrome, so add current,dict, map value as a suffix
                if word[:j] in dict and word[j:] == word[:j-1:-1]:
                    ans.append([i,dict[word[:j]]])
                #Case 2: Second part is in map, 1st part is already palindrome, so add dict,current, map value as a prefix
                if word[j:] in dict and word[:j] == word[j-1::-1]:
                    ans.append([dict[word[j:]],i])
        return ans

                


        