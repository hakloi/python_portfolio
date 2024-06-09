import xlrd, xlwt

rb = xlrd.open_workbook('ГрафДанные.xlsx')

#выбираем активный лист points
points = rb.sheet_by_index(0);