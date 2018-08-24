'''
Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.
'''


import math
import datetime

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(n):
            if n == 1: return False
            if n == 2: return True
            
            if(n%2==0): return False
            root_n = int(math.sqrt(n))
            for i in range(3,root_n+1,2):
                if(n%i==0): return False
            return True

        def is_palindrome(n):
            if n<0:
                return False
            # start_time = datetime.datetime.now()
            rev_n = int(str(n)[::-1])
            # print(datetime.datetime.now() - start_time)
            return (rev_n==n)
            # if(x%10==0 and x!=0):
            #     return False
        
            # rev_x = 0
            # while(rev_x<x):
            #     rev_x = rev_x*10+x%10
            #     x=x//10
            # return (x==rev_x or x==rev_x//10)


        while True:
            if(is_palindrome(N) and is_prime(N)):
                return N
            else:
                if(10**7<N<10**8):
                    N=10**8
                # else:
                N+=1
# print(datetime.datetime.now())
print(Solution().primePalindrome(9989900))
# print(datetime.datetime.now())