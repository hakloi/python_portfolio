f1 = input()
f2 = input()

with open(f1, "r", encoding="utf-8") as filein, \
     open(f2, "w", encoding="utf-8") as fileout:
    text = filein.read()

    while "\t" in text:
         text = text.replace("\t", "")
    while "  " in text:
         text = text.replace("  ", " ")

    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    
    fileout.write(text)
    
    
         