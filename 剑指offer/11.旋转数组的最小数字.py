# 二分查找
# 执行用时：36ms，击败88.32%
# 内存消耗：15.3MB，击败5.02%
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i,j = 0,len(numbers)-1
        if numbers[i]<numbers[j]:return numbers[0]
        while i+1<j:
            mid = (i+j)//2
            if numbers[mid] > numbers[i]:
                i = mid
            elif numbers[mid] == numbers[i]:
                i+=1
                if numbers[i] < numbers[mid]:
                    break
            else:
                j = mid
            print(i,j,mid)
        return min(numbers[i],numbers[j])
        
# 改进
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot 
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]
