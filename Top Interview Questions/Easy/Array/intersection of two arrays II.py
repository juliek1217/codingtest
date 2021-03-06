# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            i = 0
            while i < len(nums2):
                n = nums2[i]
                if n in nums1:
                    nums1.remove(n)
                    i += 1
                else:
                    nums2.remove(n)
            return nums2
        else:
            i = 0
            while i < len(nums1):
                n = nums1[i]
                if n in nums2:
                    nums2.remove(n)
                    i += 1
                else:
                    nums1.remove(n)
            return nums1
