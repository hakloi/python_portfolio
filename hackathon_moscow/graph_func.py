import openpyxl
# cleaner
import os

clear = lambda: os.system('cls')
clear()

# code
wb = openpyxl.load_workbook(filename = '../hackathon_moscow/ГрафДанные.xlsx')

points = wb['points']
val = points['A1'].value
print(val)