# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #         Python XOR on Integers
        # The XOR operator can be applied on integers as well. Internally when you invoke XOR on integers, Python converts the integers to their boolean representations and then conducts a bitwise XOR on these representations. The result is then converted back to integer notation.
        xor = 0
        for n in nums:
            xor ^= n
        return xor
