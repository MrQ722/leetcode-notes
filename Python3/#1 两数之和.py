# 自己写的第一版答案，运行时间6336ms，消耗内存14.6MB。
# 虽然也是用了两层循环，但是不是遍历全表，比两层循环要快一些。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = 0
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    a = 1
                    break
            if a == 1:
                break
        return [i,j]
    
# 可以用Pyton中list的相关函数求解
# 方法一
# 解题关键主要是想找到 num2 = target - num1，是否也在 list 中，那么就需要运用以下两个方法：
# num2 in nums，返回 True 说明有戏
# nums.index(num2)，查找第一个 num2 的索引
# 运行时间1060ms，消耗内存14.6MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = 0
            num2 = target - nums[i]
            if num2 in nums:
                if num2 !=nums[i]:
                    a = 1
                    j = nums.index(num2)
                    break
                else:
                    if nums.count(num2) != 1:
                        a = 1
                        j = nums.index(num2, i+1)
                        break
                    else:
                        continue
        if a == 0:
            return([])
        else:
            return([i,j])
        
# 方法二
# 解题思路是在方法一的基础上，优化解法。
# 想着，num2 的查找并不需要每次从 nums 查找一遍，只需要从 num1 位置之前或之后查找即可。
# 从 num1 位置之后查找：运行时间988ms，消耗内存14.9MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = 0
            temp = nums[i+1:]
            num2 = target - nums[i]
            if num2 in temp:
                a = 1
                break
        if a == 0:
            return([])
        else:
            return([i,i+1+temp.index(num2)])
# 从 num1 位置之前查找：运行时间444ms，消耗内存14.6MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(1,len(nums)):
            a = 0
            temp = nums[:i]
            num2 = target - nums[i]
            if num2 in temp:
                a = 1
                break
        if a == 0:
            return([])
        else:
            return([temp.index(num2),i])

# 方法三
# 通过哈希来求解，这里通过字典来模拟哈希查询的过程。
# 这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤。
# 运行时间48ms，消耗内存15.9MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        char = {}
        a = 0
        for i , item in enumerate(nums):
            char[item] = i
        for i , item in enumerate(nums):
            j = char.get(target-item)
            if j != None and j!=i:
                a = 1
                break  
        if a == 0:
            return([])
        else:
            return([i,j])

# 方法四
# 不需要 mun2 ，不需要在整个 dict 中去查找。可以在 num1 之前的 dict 中查找，因此就只需要一次循环可解决。
# 运行时间64ms，消耗内存15.2MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        char = {}
        a = 0
        for i , item in enumerate(nums):
            if char.get(target - item) != None:
                a = 1
                break     
            char[item] = i
        if a == 0:
            return([])
        else:
            return([char.get(target - item),i])
