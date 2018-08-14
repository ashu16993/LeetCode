'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        longest_common_prefix = strs[0]
        
        # print(longest_common_prefix)
        for word in strs:
            if word=="":
                return ""
            if(word==longest_common_prefix):
                continue
            if(word[0]!=longest_common_prefix[0]):
                longest_common_prefix=""
                break
            # print(longest_common_prefix)
            for i in range(len(word)):
                # print(i)
                if(i>len(longest_common_prefix)-1 or word[i] is not longest_common_prefix[i]):
                    longest_common_prefix=longest_common_prefix[:i]
                    break
                # print(longest_common_prefix)
            if(len(word)<len(longest_common_prefix)):
                longest_common_prefix = word
        return(longest_common_prefix)
        


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","fl"]))