nums = [1,1,1,2,2,3]
dupl_dct = {}
for el in nums:
    if el not in dupl_dct:
        dupl_dct[el] = 1
    if el in dupl_dct and dupl_dct[el] < 2:
        dupl_dct[el] += 1
    if dupl_dct[el] >= 2:
        nums.pop(el)

for k,v in dupl_dct.items():
    print(k, v)
print(len(nums))