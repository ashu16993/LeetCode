'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Solved using divide and conquer 
from math import ceil
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(isBadVersion(1)==True):
            return 1
        if(isBadVersion(n)==False):
            return -1
        high = n
        low = 0
        cursor = ceil((high+low)/2)
        print(cursor)
        while(cursor>=1 and cursor<=n):
            if(isBadVersion(cursor)==True):
                if(cursor!=1):
                    if(isBadVersion(cursor-1)==True):
                        high = cursor
                    else:
                        return cursor
                else:
                    return 1
            else:
                low = cursor
            cursor = ceil((high+low)/2)
            print(2,high,low,cursor)
        return -1