# 字典统计出现次数，set去重、
# 执行用时：32ms，击败100%
# 内存消耗：13.7MB，击败5.42%

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        char = {}
        for i in arr:
            if i in char:
                char[i] += 1
            else:
                char[i] = 1
        value = char.values()
        if len(set(value)) == len(value):
            return True
        else:
            return False
            
# 用get可以化简
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        s=[d[i] for i in d]
        return len(set(s))==len(s)
