import re

def normalize(text):
    return set(re.findall(r'\w+', text.lower()))

with open('library_input.txt', 'r', encoding='utf-8') as f:
    lines = f.read().strip().split('\n')

n = int(lines[0])
documents = [lines[i+1].strip() for i in range(n)]
m = int(lines[n+1])
requests = [lines[n+2+i].strip() for i in range(m)]

normalized_docs = [normalize(doc) for doc in documents]

with open('library_output.txt', 'w', encoding='utf-8') as f:
    f.write(f"{m}\n")
    for req in requests:
        norm_req = normalize(req)
        scores = [(len(norm_req & nd), i) for i, nd in enumerate(normalized_docs)]
        top5 = sorted(scores, key=lambda x: -x[0])[:5]
        f.write(f"{len(top5)}\n")
        for _, i in top5:
            f.write(documents[i] + '\n')
