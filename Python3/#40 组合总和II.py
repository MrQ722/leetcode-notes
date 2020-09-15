# 回溯（嵌套函数）
# 这道题主要需要注意重复的数据，因此在helper内的循环开始进行判断，使得在同一层级的重复数据直接跳过
# 注意其中列表tem的更新，注意pop()的用法
# 难度较高
# 运行时间36ms，消耗内存13.5MB
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sub = []
        tem = []
        candidates.sort()
        def helper(tar,tem,start):
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if tar == candidates[i]:
                    tem.append(candidates[i])
                    sub.append(tem[:])
                    tem.pop()
                    break
                elif tar < candidates[i]:
                    break
                else:
                    tem.append(candidates[i])
                    helper(tar-candidates[i],tem,i+1)
                    tem.pop()
        helper(target,tem,0)
        return sub
