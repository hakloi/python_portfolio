def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    print(nums1, nums2)
    
    res = []
    
    i, j = 0, 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
    
    return res
    
nums1 = [4, 4, 9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))

# for i in range(len(nums1)):
#     for j in range(len(nums2)):
#         print(nums1[i], nums2[j])