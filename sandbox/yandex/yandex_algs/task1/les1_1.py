# O(n)
phrase = "pompeii was a large roman town in campania italy which was buried in volcanic ash following the eruption of mt vesuvius in 79 ad"
print(len(phrase))

freq ={}

for i in phrase:
    if i in freq:
        freq[i]+= 1
    else: 
        freq[i] = 1
    
print("Counter of all elements in phrase : " + str(freq))