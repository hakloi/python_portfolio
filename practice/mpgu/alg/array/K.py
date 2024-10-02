marks = list(map(int, input().split()))
grades = marks[1:]
max_grade = max(grades)
min_grade = min(grades)

res = [min_grade if grade == max_grade else grade for grade in grades]  
print(*res)