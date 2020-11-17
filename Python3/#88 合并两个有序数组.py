# 一次遍历，pop+insert
# 执行用时：56ms，击败5.06%
# 内存消耗：13.5MB，击败25.19%
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
        while j<n:
            if nums2[j] <= nums1[i] or i  == m + j:
                print(i,j)
                nums1.pop()
                nums1.insert(i,nums2[j])
                j+=1
            i+=1
            
# 合并后排序
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

