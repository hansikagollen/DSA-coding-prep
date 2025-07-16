class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Acronym: TRBL (like "TROUBLE")
        # T → Top row (left to right)
        # R → Right column (top to bottom)
        # B → Bottom row (right to left)
        # L → Left column (bottom to top)
        # After T → top += 1
        # After R → right -= 1
        # After B → bottom -= 1
        # After L → left += 1

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        res = []
        while len(res) < rows * cols:
            # T
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # R
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # B
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # L
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res