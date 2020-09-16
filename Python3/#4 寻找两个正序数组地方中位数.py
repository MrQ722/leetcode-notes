# 最初的想法是分别从两个列表的两端进行比较，比较次数肯定小于两个list和的一半
# 但是由于两个list的和可能为奇数或者偶数，因此需要很多的分支语句，放弃了这种想法
# 最后，应用list自带的sort()语句对两个list的拼接进行排序，直观求出中位数
# 执行用时：48ms，击败93.28%
# 内存消耗：13.4MB，击败71.20%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        a = len(nums1)
        b = len(nums2)
        if (a+b)%2 == 1:
            med = nums[(a+b)//2]
        else:
            med = (nums[(a+b)//2-1] + nums[(a+b)//2])/2
        return med

# 可以转化成寻找第k小数的问题
# 方法一：用两个指针分别扫描两个数组，比较两个值的大小，移动指针得出第k小数
# 自己写的代码，冗余比较多
# 执行用时：56ms，击败70.65%
# 内存消耗：13.5MB，击败25.42%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)
        nums1.append(0)
        nums2.append(0)
        global i,j
        i = 0
        j = 0
        def helper(time):
            global i,j
            for k in range(time):
                if nums1[i] < nums2[j]:
                    if i == a:
                        j += 1
                    else:
                        i += 1
                else:
                    if j == b:
                        i += 1
                    else:
                        j += 1
            if i == a:
                return nums2[j]
            elif j ==b:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                return nums1[i]
            else :
                return nums2[j]
        if (a+b)%2 == 1:
            time = (a+b)//2
            if time == 0:
                return sum(nums1+nums2)
            else:
                return helper(time)
        else:
            time = (a+b)//2 - 1
            if time == 0:
                return sum(nums1+nums2)/2
            else:
                return ((helper(time) + helper(1))/2)

# 方法二：折半删除，注意证明，在删除数组的最大值右侧包含有第k小数，因此方法可行
# 代码很多，略
