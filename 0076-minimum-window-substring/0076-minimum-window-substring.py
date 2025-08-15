class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wind_cntr = Counter()
        target_cntr = Counter(t)
        ans = ""
        i, j = 0, 0
        
        while j < len(s):
            # Expand window until all chars in `t` are included
            while j < len(s) and len(target_cntr - wind_cntr) > 0:
                wind_cntr[s[j]] += 1
                j += 1
            
            # Shrink window to find the minimal valid substring
            while i < j and len(target_cntr - wind_cntr) == 0:
                if not ans or j - i < len(ans):
                    ans = s[i:j]
                wind_cntr[s[i]] -= 1
                i += 1
        
        return ans