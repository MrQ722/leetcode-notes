class Solution:
    def numWays(self, n: int) -> int:
        x1 = 1
        x2 = 1
        for i in range(n):
            x1,x2 = x2,x1+x2
        return x1%(10**9+7)
