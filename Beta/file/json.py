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

# a = int(input())
# b = int(input())
# c = int(input())

# max_num = max(a, b, c) ** 2 * 2
# solve = a ** 2 + b ** 2 + c ** 2

# if max_num == solve:
#      print("100%")
# elif max_num > solve:
#      print("велика")
# else:
#      print("крайне мала")

# f1 = input()
# f2 = input()
# f3 = input()
# f4 = input()

# with open(f1, "r", encoding="utf-8") as filein:
#      all = []
#      for line in filein:
#           nums = line.split()
#           all += nums
     
#      even = []
#      odd = []
#      eq = []
#      for el in all:
#           dct = {'ev': 0, 'odd': 0}
#           for ch in el:
#                if (int(ch) % 2 == 0):
#                     dct['ev'] += 1
#                else:
#                     dct['odd'] += 1
          
#           if dct['ev'] == dct['odd']:
#                eq.append(el)
#           elif dct['ev'] > dct['odd']:
#                even.append(el)
#           else:
#                odd.append(el)
     
# with open(f2, "w", encoding="utf-8") as evenf:
#      evenf.write(" ".join(even))     
     
# with open(f3, "w", encoding="utf-8") as oddf:
#      oddf.write(" ".join(odd))  
     
# with open(f4, "w", encoding="utf-8") as eqf:
#      eqf.write(" ".join(eq))  