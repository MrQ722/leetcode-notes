# 不难
# 执行用时：140ms，击败66.08%
# 内存消耗：16.9MB，击败62.01%
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:return 0
        points.sort()
        n,key = 1,points[0][-1]
        for i in range(1,len(points)):
            if points[i][0]<=key:
                if points[i][-1]<key:
                    key = points[i][-1]
                continue
            else:
                key = points[i][-1]
                n+=1
        return n
