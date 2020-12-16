# 递归
# 超出时间限制
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False
        def helper(i,j):
            if matrix[i][j] == target:return True
            elif matrix[i][j]>target:return False
            else:
                if i+1<len(matrix) and j+1<len(matrix[0]):
                    if matrix[i+1][j] > matrix[i][j+1]:
                        if helper(i+1,j):return True
                        if helper(i,j+1):return True
                        return False
                    else:
                        if helper(i,j+1):return True
                        if helper(i+1,j):return True
                        return False
                else:
                    if i+1<len(matrix):
                        if helper(i+1,j):return True
                    if j+1<len(matrix[0]):
                        if helper(i,j+1):return True
                    return False
        return helper(0,0)

# 暴力解法
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            for y in x:
                if y == target:
                    return True
        return False
        
# 线性查找
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False
        i,j = 0,len(matrix[0])-1
        while i<len(matrix) and j>=0:
            if matrix[i][j] > target:
                j-=1
            elif matrix[i][j] == target:
                return True
            else:
                i+=1
        return False
