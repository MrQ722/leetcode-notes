# 一次遍历
# 执行用时：224ms，击败：98.45%
# 内存消耗：14.9MB，击败：15.83%

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A:return A
        a = A[0]
        key = 0
        for i in range(1,len(A)):
            if A[i] > a:
                a = A[i]
                key = i
            else:
                break
        if key == 0:return False
        if key == len(A) - 1: return False
        for i in range(key+1,len(A)):
            if A[i] < a:
                a = A[i]
            else:
                return False
        return True

# 官方答案（类似）
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # 递增扫描
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # 最高点不能是数组的第一个位置或最后一个位置
        if i == 0 or i == N - 1:
            return False

        # 递减扫描
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1



# 双指针
# 执行用时：304ms，击败：13.06%
# 内存消耗：14.9MB，击败：14.39%

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:return False
        i, j = 0, len(A)-1
        for k in range(len(A)):
            if i+1<len(A) and A[i] < A[i+1]:
                i+=1               
            if j-1>=0 and A[j] < A[j-1]:
                j-=1         
        if i == j and i > 0 and j < len(A)-1:return True
        else:return False
