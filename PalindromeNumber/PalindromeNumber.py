class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the number to a string
        str_x = str(x)
        
        # Check if the string reads the same forwards and backwards
        return str_x == str_x[::-1]

# Example usage:
solution = Solution()
print(solution.isPalindrome(121))    # Output: true
print(solution.isPalindrome(-121))   # Output: false
print(solution.isPalindrome(10))     # Output: false
