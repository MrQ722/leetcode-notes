# 递归+个人觉得很优雅
# 超出时间限制
# 自底向上的动态规划会在每个下标都进行大量的匹配，导致超时
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:return []
        tmp = []
        for i in range(1,len(s)+1):
            if s[0:i] in wordDict:
                if i == len(s):
                    tmp.append(s[0:i])
                else:
                    for x in self.wordBreak(s[i:],wordDict):
                        tmp.append(s[0:i]+' '+x)
        return tmp

# 为了避免动态规划的方法超时，需要首先使用第 139 题的代码进行判断，在可以拆分的情况下再使用动态规划的方法进行拆分。
# 相比之下，自顶向下的记忆化搜索可以在搜索过程中将不可以拆分的情况进行剪枝，因此记忆化搜索是更优的做法。


# 记忆化搜索
# 使用哈希表存储字符串s的每个下标和从该下标开始的部分可以组成的句子列表，
# 在回溯过程中如果遇到已经访问过的下标，则可以直接从哈希表得到结果，而不需要重复计算。
# 如果到某个下标发现无法匹配，则哈希表中该下标对应的是空列表，因此可以对不能拆分的情况进行剪枝优化。
# 貌似跟自己写的一样
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans
        
        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]


    
# 回溯+记忆字符串是否可分
class Solution:
    # 带备忘录的记忆化搜索
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        memo = [1] * (len(s)+1)
        wordDict = set(wordDict)

        def dfs(wordDict,temp,pos):
            num = len(res)                  # 回溯前先记下答案中有多少个元素
            if pos == len(s):
                res.append(" ".join(temp))
                return
            for i in range(pos,len(s)+1):
                if memo[i] and s[pos:i] in wordDict: # 添加备忘录的判断条件
                    temp.append(s[pos:i])
                    dfs(wordDict,temp,i)
                    temp.pop()
            # 答案中的元素没有增加，说明s[pos:]不能分割，修改备忘录        
            memo[pos] = 1 if len(res) > num else 0 
            
        dfs(wordDict,[],0)
        return res

