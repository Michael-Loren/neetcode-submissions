class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            rows = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] not in rows:
                    rows.add(board[r][c])
                else:
                    return False
        

        for c in range(9):
            cols = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] not in cols:
                    cols.add(board[r][c])
                else:
                    return False

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                box = set()
                for r in range(3):
                    for c in range(3):
                        if board[x + r][y + c] == ".":
                            continue
                        elif board[x + r][y + c] not in box:
                            box.add(board[x + r][y + c])
                        else:
                            return False
        return True
                        

