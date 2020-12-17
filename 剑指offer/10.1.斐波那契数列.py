class Solution:
    def fib(self, n: int) -> int:
        x1 = 0
        x2 = 1
        for i in range(1,n):
            x2 += x1
            x1 = x2 - x1
        return x2%(10**9+7) if n>0 else 0
        
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
