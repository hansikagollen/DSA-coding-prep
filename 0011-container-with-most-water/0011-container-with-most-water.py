class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        ans = 0

        while i < j:
            mini = min(height[i], height[j])
            ans = max(ans, mini * (j - i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return ans