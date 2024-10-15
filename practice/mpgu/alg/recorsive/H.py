# def chip(place, seq=None):
#     if seq is None:
#         seq = []
#     if place == 1:
#         seq.append(1)
#     else:
#         chip(place - 1, seq)  
#         seq.append(place)
#         seq.append(-1 * (place - 1)) 
#         seq.append(place) 
#     return seq

# places = int(input())
# res = chip(places)
# print(*res)

# 3
# 1 2 -1 3 1
