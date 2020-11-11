# 递归
# 超出时间限制
# 测试用例："caotmcaataijjxi"
#          "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        if not key:return 0
        tmp = []
        for i in range(len(ring)):
            if ring[i] == key[0]:
                n = self.findRotateSteps(ring[i:]+ring[:i],key[1:]) if len(key)>1 else 0
                tmp.append(min(i,len(ring)-i)+n)
        return min(tmp)+1


# DFS
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        import collections, functools
        lookup = collections.defaultdict(list)
        for i in range(len(ring)):
            lookup[ring[i]].append(i)


        @functools.lru_cache(None)
        def dfs(cur, k):
            if k == len(key):
                return 0
            res = float("inf")
            for j in lookup[key[k]]:
                res = min(res, min(tmp:= abs(cur - j), len(ring) - tmp) + 1 + dfs(j, k + 1))
            return res

        return dfs(0, 0)
