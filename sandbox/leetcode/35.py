# You must write an algorithm with O(log n) runtime complexity.

def search_insert_pos(nums, target):
    if len(nums) >= 0:
        mid = len(nums) // 2
        if nums[mid] == target:
            return nums.index(target)
        elif nums[mid] > target:
            return search_insert_pos(nums[:mid], target)
        elif nums[mid] < target:
            return search_insert_pos(nums[mid:], target)
        

nums = [1,3,5,6]
target = 5
print(search_insert_pos(nums, target))