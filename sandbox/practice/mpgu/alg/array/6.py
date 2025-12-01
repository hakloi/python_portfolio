n, m = map(int, input().split())
anya = [int(input()) for _ in range(n)]
borya = [int(input()) for _ in range(m)]

set_anya = set(anya)
set_borya = set(borya)

common_set = set_anya & set_borya
unique_anyas = set_anya - common_set
unique_boryas = set_borya - common_set

print(len(common_set))
print(*sorted(common_set))
print(len(unique_anyas))
print(*sorted(unique_anyas))
print(len(unique_boryas))
print(*sorted(unique_boryas))