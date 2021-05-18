class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        if not len(nums)%2 == 0:
          return nums[int(len(nums)/2)]
        else :
        return (nums[int(len(nums)/2) - 1] + nums[int(len(nums)/2)]) / 2
