'''There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example :
    Input : [1,3,5,7]
            [2,9,12]
    Output : 5'''


def get_median(nums):
    median = 0
    if len(nums)==0:
        return 0
    if(len(nums)%2==0):
        median = (nums[(len(nums)//2)-1]+nums[(len(nums)//2)])/2
    else:
        median = nums[len(nums)//2]
    return median


'''This is the solution as explained online'''
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median1 = get_median(nums1)        
        median2 = get_median(nums2)
        if len(nums1)==0 or len(nums2)==0:
            return median1+median2
        # return((median1+median2)/2)
        else:
            return median(nums1,nums2)


if __name__=="__main__":
    print(Solution().findMedianSortedArrays([1,2,3,4,5,8,9],[8,11,12,13]))