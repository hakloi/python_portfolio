citations = [3,0,6,1,5]

papers = len(citations)
bucket = [0] * (papers + 1)

for cit in citations:
    bucket[min(cit, papers)] += 1
    
cumalitive = 0
for h_index in range(papers, -1, -1):
    cumalitive += bucket[h_index]
    
    if cumalitive >= h_index:
        print(h_index)