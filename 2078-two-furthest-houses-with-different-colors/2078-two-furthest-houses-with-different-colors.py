class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distance=0
        for x,y in enumerate(colors):
            if y!=colors[0]:
                distance=max(distance,x)

            if y!=colors[-1]:
                distance=max(distance,len(colors)-1-x)
        return distance


        