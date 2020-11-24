# 贪心算法
# 执行用时：76ms，击败8.77%
# 内存消耗：13.5MB，击败22.58%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            a,b,c = [],[],[]
            for j in range(9):
                if board[i][j] in a:
                    return False
                elif board[i][j] != '.':
                    a.append(board[i][j])
                if board[j][i] in b:
                    return False
                elif board[j][i] != '.':
                    b.append(board[j][i])
                if board[3*(i//3)+j//3][3*(i%3)+j%3] in c:
                    return False
                elif board[3*(i//3)+j//3][3*(i%3)+j%3] != '.':
                    c.append(board[3*(i//3)+j//3][3*(i%3)+j%3])
        return True
               
               
# 一次遍历
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True
