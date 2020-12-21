# dfs
# 执行用时：744ms，击败5.03%
# 内存消耗：17.2MB，击败5.00%
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        tmp = []

        def dfs(i,j):
            if not 0 <= i < m or not 0 <= j < n or sum([int(x) for x in str(i)]) + sum([int(x) for x in str(j)]) > k:return 
            if (i,j) in tmp:return 
            tmp.append((i,j))
            dfs(i+1,j);dfs(i-1,j);dfs(i,j+1);dfs(i,j-1)

        dfs(0,0)
        return(len(tmp)) 
        
# 广度优先搜索
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)


# 递推
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)
