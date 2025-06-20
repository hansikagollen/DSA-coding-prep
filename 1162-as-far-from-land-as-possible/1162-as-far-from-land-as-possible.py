class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        land = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    land.append((i, j))

        if not land or len(land) == n * m:
            return -1

        result = -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    wasd = False
                    #upar niche dayne byne
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                            result = max(result, 1)
                            wasd = True
                            break
                    if not wasd:
                        min_dist = float('inf')
                        for lx, ly in land:
                            dist = abs(lx - i) + abs(ly - j)
                            if dist < min_dist:
                                min_dist = dist
                        result = max(result, min_dist)
        del grid
        del land
        return result