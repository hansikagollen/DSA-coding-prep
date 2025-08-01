class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans=0
        north=south=east=west=0
        for i in range(len(s)):
            c=s[i]
            if c=='N':
                north+=1
            elif c=='S':
                south+=1
            elif c=='E':
                east+=1
            elif c=="W":
                west+=1

            x=abs(north-south)
            y=abs(east-west)
            Manhattan_distance=x+y
            dis=Manhattan_distance+(min(2*k,i+1-Manhattan_distance))
            ans=max(ans,dis)

        return ans




        