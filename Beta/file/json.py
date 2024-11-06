# f1 = input()
# f2 = input()

# with open(f1, "r", encoding="utf-8") as filein, \
#      open(f2, "w", encoding="utf-8") as fileout:
#     text = filein.read()

#     while "\t" in text:
#          text = text.replace("\t", "")
#     while "  " in text:
#          text = text.replace("  ", " ")

#     text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    
#     fileout.write(text)
    
    
# f = input()
# n = int(input())

# with open(f, "r", encoding="utf-8") as filein:
#     lines = filein.readlines()
#     reverse = lines[-n:]
#     for line in reverse:
#          print(line.strip())

# Также можно использовать соотношение квадратов сторон, если одна из них (с) — наибольшая, а две другие (a и b): 3

# c2 < a2 + b2 — треугольник остроугольный; 3
# c2 = a2 + b2 — треугольник прямоугольный; 3
# c2 > a2 + b2 — треугольник тупоугольный. 3

a = int(input())
b = int(input())
c = int(input())

max_num = max(a, b, c) ** 2 * 2
solve = a ** 2 + b ** 2 + c ** 2

if max_num == solve:
     print("100%")
elif max_num > solve:
     print("велика")
else:
     print("крайне мала")