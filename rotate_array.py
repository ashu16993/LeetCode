'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

from math import gcd
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==1:
            return

        # after a cycle of shift when k=n, it will lead to the original array itself
        if k>n:
            k = k%n
        
        # Right shift using gcd logic, i.e shifting by swapping values
        # Check geekforgeek for better explanation https://www.geeksforgeeks.org/array-rotation/ 
        for i in range(gcd(k,n)):
        # move i-th values of blocks 
            temp = nums[n-i-1]
            j = i
            while 1:
                m = j + k
                # print(m)
                if m >= n:
                    m = m - n
                if m == i:
                    break
                # print(n-j,n-m)
                nums[n-j-1] = nums[n-m-1]
                j = m
            # print(i,temp)
            nums[k-1-i] = temp
        return nums

# nums = [1,2,3,4,5,6,7,8,9,10,11,12]
nums = [1,2]
print(Solution().rotate(nums,3))
