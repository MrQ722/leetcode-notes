# 二次遍历
# 执行用时：204ms，击败34.14%
# 内存消耗：15.8MB，击败14.10%
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        tmp = []
        for i in range(R):
            for j in range(C):
                tmp.append((abs(i-r0)+abs(j-c0),[i,j]))
        tmp.sort()
        return [x[-1] for x in tmp]

# 简化
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ret = [(i, j) for i in range(R) for j in range(C)]
        ret.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return ret

# 几何法
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                    row += dr
                    col += dc
        return ret



         
