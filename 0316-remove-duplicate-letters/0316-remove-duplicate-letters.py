class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index={char:i for i,char in enumerate(s)}  #last occurence of char
        stack=[]
        seen=set()

        for i,char in enumerate(s):
            if char in seen:
                continue #skip if already in result
             # Remove characters that are greater than current and appear later
            while stack and char<stack[-1] and i<last_index[stack[-1]]:
                removed=stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)
        return ''.join(stack)
        