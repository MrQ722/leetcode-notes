# 寻找所需合并的区间的起始点和终止点
# 执行用时：40ms，击败93.88%
# 内存消耗：15.1MB，击败19.24%
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:return [newInterval]
        sub = []
        start = newInterval[0]
        end = newInterval[1]
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                start = newInterval[0]
                break
            else:
                if newInterval[0] <= intervals[i][1]:
                    start = intervals[i][0]
                    break
                else:
                    continue
        for i in range(len(intervals)-1,-1,-1):
            if newInterval[1] > intervals[i][1]:
                end = newInterval[1]
                break
            else:
                if newInterval[1] >= intervals[i][0]:
                    end = intervals[i][1]
                    break
                else:
                    continue
        for inter in intervals:
            if inter[0]>=start and inter[1]<=end:
                continue
            else:
                sub.append(inter)
        sub.append([start,end])
        sub.sort()
        return sub
