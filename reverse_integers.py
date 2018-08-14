'''
Given a 32-bit signed integer, reverse digits of an integer.
Input: 123
Output: 321

Input: 120
Output: 21

Input: -123
Output: -321

'''



class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # print(x)
        rev_x = 0
        mult_flag = 1
        print(abs(x),2**31-1)
        # if abs(x)>((2**31)-1):
        #     return 0
        if x<0:
            mult_flag = -1
            x=x*-1
        
        # Mathematical way
        # while(x!=0):
        #     rev_x = rev_x*10 + x%10
        #     x=x//10
        
        # Pythonic way
        rev_x=str(x)[::-1]
        rev_x=int(rev_x)

        if abs(rev_x)>((2**31)-1):
            return 0
        return(mult_flag*rev_x)

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
            
            ret = Solution().reverse(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()