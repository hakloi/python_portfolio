# import json
# from sys import stdin

# ans = [int(line.strip()) for line in stdin]

# with open("scoring.json", "r", encoding="utf-8") as filein:
#     data = json.load(filein)

# res_patt = {}
# global_test_index = 1

# for part in data:
#     points = part["points"]
#     tests = part["tests"]
#     point_for_task = points / len(tests)  
    
#     for test in tests:
#         res_patt[global_test_index] = {
#             "pattern": int(test["pattern"]), 
#             "points": point_for_task
#         }
#         global_test_index += 1

# total_score = 0
# for i, user_ans in enumerate(ans, 1): 
#     if i in res_patt and user_ans == res_patt[i]["pattern"]:
#         total_score += res_patt[i]["points"]

# print(int(total_score))


# 4
# 12
# 3
# 100
# 0

from sys import stdin
import json

with open('scoring.json') as file:
    data = json.load(file)

answers = stdin.readlines()

score = 0

for tests in data:
    point = int(tests['points'] / len(tests['tests']))
    for test in tests['tests']:
        result = test['pattern']
        for answer in answers:
            if result == answer.strip('\n'):
                score += point

print(score)