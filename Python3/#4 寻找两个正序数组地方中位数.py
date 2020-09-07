# 最初的想法是分别从两个列表的两端进行比较，比较次数肯定小于两个list和的一半
# 但是由于两个list的和可能为奇数或者偶数，因此需要很多的分支语句，放弃了这种想法
# 最后，应用list自带的sort()语句对两个list的拼接进行排序，直观求出中位数
# 运行时间56ms，消耗内存13.7MB
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
