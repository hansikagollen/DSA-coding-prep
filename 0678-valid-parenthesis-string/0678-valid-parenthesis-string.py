class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        string=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]=='*':
                string.append(i)
            else:
                if stack:
                    stack.pop()
                elif string:
                    string.pop()
                else:
                    return False
        while stack:
            if len(string)==0:
                return False
            elif stack[-1]<string[-1]:
                stack.pop()
                string.pop()
            else:
                return False
        return True
        