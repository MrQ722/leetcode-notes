# 元组排序
# 执行用时：44ms，击败96.02%
# 内存消耗：13.7MB，击败6.32%
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        sub = []
        for i in range(len(arr)):
            sub.append((str(bin(arr[i])).count('1'),arr[i]))
        sub.sort()
        return [x[1] for x in sub]
