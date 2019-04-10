'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and nums2:
            if len(nums2)%2 == 1:
                return nums2[int(len(nums2)/2)]
            else:
                return (nums2[int(len(nums2)/2)-1] + nums2[int(len(nums2)/2)]) / 2
        if not nums2 and nums1:
            if len(nums1)%2 == 1:
                return nums1[int(len(nums1)/2)]
            else:
                return (nums1[int(len(nums1)/2)-1] + nums1[int(len(nums1)/2)]) / 2
        res = []
        i , j = 0 , 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        if i < len(nums1):
            for k in range(i , len(nums1)):
                res.append(nums1[k])
        if j < len(nums2):
            for k in range(j , len(nums2)):
                res.append(nums2[k])
        if len(res)%2 == 1:
            return res[int(len(res)/2)]
        else:
            return (res[int(len(res)/2)-1] + res[int(len(res)/2)]) / 2
#题目要求是O(log(m+n))，但是我的算法涉及到数组的迁移，所以时间复杂度是O(n)

class Solution:
    def median(A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
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
