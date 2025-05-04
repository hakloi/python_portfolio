def intersection(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)

    return list(s1 & s2)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))