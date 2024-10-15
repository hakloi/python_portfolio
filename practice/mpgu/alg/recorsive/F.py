def reverse():
    w = int(input())  
    if w != 0:  
        reverse() 
    print(w)  

reverse() 

# Примеры
# входные данные
# 1
# 2
# 3
# 0
# выходные данные
# 0
# 3
# 2
# 1