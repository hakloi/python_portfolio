n = int(input())
array = set(map(int, input().split()))  # set чтобы были только уникальные элементы
target = int(input())
count = 0 

while True:
    if target - count in array:
        print(target - count)
        break
    elif target + count in array:
        print(target + count)
        break
    count += 1
