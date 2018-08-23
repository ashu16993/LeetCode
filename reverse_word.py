'''
Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s= s.strip().split(' ')
        
        s= [x for x in s if x!='']
        # print(s)
        for i in range(len(s)//2):
            s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
        # print(s)
        return " ".join(s)




print(Solution().reverseWords("   ashu    is awesome   and  you aren't muha ahahaha"))
