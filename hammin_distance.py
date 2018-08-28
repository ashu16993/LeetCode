'''The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.'''



class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        # Just to implement my own int to binary function
        def intToBinary(number):
            binarynumber=""
            if (number!=0):
                while (number>=1):
                    if (number %2==0):
                        binarynumber=binarynumber+"0"
                        number=number/2
                    else:
                        binarynumber=binarynumber+"1"
                        number=(number-1)/2

            else:
                binarynumber="0"

            return "".join(reversed(binarynumber))

        # print(intToBinary(x),format(x,'0b'))
        # print(intToBinary(y),format(y,'0b'))

        # To find which bits are different XOR operator will help(Check its truth table)
        # print(intToBinary(x^y))
        x_xor_y = intToBinary(x^y)

        distance = sum(int(i) for i in x_xor_y)
        return distance



print(Solution().hammingDistance(1,4))



        