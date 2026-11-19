class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnDic = defaultdict(set)
        rowDic = defaultdict(set)
        squareDic = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if (board[row][col] in columnDic[col]
                    or board[row][col] in rowDic[row]
                    or board[row][col] in squareDic[(row // 3, col // 3)]):
                    return False
                else:
                    columnDic[col].add(board[row][col])
                    rowDic[row].add(board[row][col])
                    squareDic[(row // 3, col // 3)].add(board[row][col])

        return True