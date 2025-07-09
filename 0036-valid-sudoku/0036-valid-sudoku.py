class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(9):
            nums = set("123456789")
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in nums:
                    nums.remove(board[i][j])
                else:
                    return False

        #columns
        for i in range(9):
            nums = set("123456789")
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in nums:
                    nums.remove(board[j][i])
                else:
                    return False


        #3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                nums = set("123456789")
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val == ".":
                            continue
                        elif val in nums:
                            nums.remove(val)
                        else:
                            return False

        return True