'''Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        print(len(s))
        substring = {}
        len_substring = 0
        j = 0
        for i in range(len(s)):
            # print(i,s[i])
            if s[i] in substring:
                # substring={}
                j = max(substring[s[i]],j)
                # len_substring.append(len_substring[i-1]-substring[s[i]]+1)
            # else:
            #     if(i==0):
            #         len_substring.append(1)
            #     else:
            #         len_substring.append(len_substring[i-1]+1)
            # print(len_substring,i-j+1,j)
            len_substring = max(len_substring,i-j+1)
            substring[s[i]] = i+1
            # print(max(len_substring),len_substring)
        return len_substring

def stringToString(input):
    return input[1:-1]

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()