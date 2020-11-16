# 执行用时：48ms，击败：77.88%
# 内存消耗：13.5MB，击败27.10%
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        tmp = []
        for x in arr2:
            while x in arr1:
                tmp.append(x)
                arr1.remove(x)
        arr1.sort()
        return tmp+arr1
