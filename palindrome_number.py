'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward
Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        
        # Pythonic way
        # rev_x = int(str(x)[::-1])
        # return (rev_x==x)

        # Alternate way
        # By reversing just half of the number
        # To check when we have reached half of the number.. 
        # it should have lesser digits than its reversed part

        # First remove the corner case of last digit being 0
        if(x%10==0 and x!=0):
            return False
        
        rev_x = 0
        while(rev_x<x):
            rev_x = rev_x*10+x%10
            x=x//10
        return (x==rev_x or x==rev_x//10)




def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            x = int(line);
            
            ret = Solution().isPalindrome(x)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()