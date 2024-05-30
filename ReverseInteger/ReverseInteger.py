class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Store the sign of x
        sign = -1 if x < 0 else 1
        
        # Work with the absolute value of x
        x = abs(x)
        
        # Initialize the reversed integer to 0
        reversed_x = 0
        
        # Reverse the digits
        while x != 0:
            # Pop the last digit from x
            pop = x % 10
            x //= 10
            
            # Check for overflow and underflow
            if reversed_x > (INT_MAX - pop) // 10:
                return 0
            
            # Push the digit to reversed_x
            reversed_x = reversed_x * 10 + pop
        
        # Restore the sign
        reversed_x *= sign
        
        return reversed_x

# Example usage:
solution = Solution()
print(solution.reverse(123))    # Output: 321
print(solution.reverse(-123))   # Output: -321
print(solution.reverse(120))    # Output: 21
print(solution.reverse(1534236469))  # Output: 0 (since it overflows)
