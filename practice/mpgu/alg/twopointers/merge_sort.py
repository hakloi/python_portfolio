# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# def merge(nums1, m, nums2, n):
#     i = m - 1
#     j = n - 1
#     k = n + m - 1
    
#     while i >= 0 and j >= 0:
#         if nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -=1
    
#     nums1[:j + 1] = nums2[:j + 1]
#     return nums1

# nums1 = []
# m = 0
# nums2 = [2]
# n = 1
# print(merge(nums1, m, nums2, n))

# def removeElement(nums, val):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1
        
#     return k
    

# Output: 5, nums = [0,1,4,0,3,_,_,_]

# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(removeElement(nums, val))

s1 = input()
s2 = input()
s3 = input()
num = []

if "зайка" in s1:
    num.append(s1)
if "зайка" in s2:
    num.append(s2)
if "зайка" in s3: 
    num.append(s3)

min_s = min(num)
print(min_s, len(min_s))
    
# зайка березка
# березка зайка
# березка елочка березка

# березка зайка 13

