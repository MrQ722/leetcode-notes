# 暴力解法，两层循环，超时
# 添加了一些限制之后，仍然超时
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        for i in range(len(height)-1):
            if maxA/(len(height)-i-1) > height[i]:
                continue
            for j in range(len(height)-1,i,-1):
                if maxA/(j-i) > height[i]:
                    break
                A = min(height[i],height[j])*(j-i)
                if A >maxA:
                    maxA = A
        return maxA

# 双指针法
# 执行用时：64ms，击败85.69%
# 内存消耗：14.6MB，击败89.70%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        maxA = 0
        while i != j:
            A = min(height[i],height[j])*(j-i)
            if A > maxA :
                maxA = A
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxA
