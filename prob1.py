# Time Complexity : O(logN)
# Space Complexity : O(1) as no extra space
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Took me a little while to understand the logic 
# and get the code correct in Python

# approach:
# keep dividing the power n by half, if n is 0, return 1, if n is 1, return x, 
# if n is -1, return 1/x
# if n is even, return pow(x, n // 2) ** 2
# else, return (pow(x, n // 2) ** 2) * x



class Solution:
    def myPow(self, x, n):
        # base
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return (1/x)
        
        # logic
        result = self.myPow(x, n // 2)
        if n % 2 == 0:
            return result * result
        else:
            return result * result * x