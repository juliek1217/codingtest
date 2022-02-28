# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Discard all spaces from the beginning of the input string.
        while index < n and s[index] == ' ':
            index += 1

        # sign = +1, if it's positive number, otherwise sign = -1.
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1

        # Traverse next digits of input and stop if it is not a digit.
        # End of string is also non-digit character.
        while index < n and s[index].isdigit():
            digit = int(s[index])

            # Check overflow and underflow conditions.
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
                return INT_MAX if sign == 1 else INT_MIN

            # Append current digit to the result.
            result = 10 * result + digit
            index += 1

        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result
