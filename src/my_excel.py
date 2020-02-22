import xlrd
import  xlwt
from xlutils.copy import  copy

def write_from_list(lst_alllines,file_name):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('请购执行进度表')
    for row, exec_line in enumerate(lst_alllines):
        for col, value in enumerate(exec_line):
            worksheet.write(row, col, value)
            width = (len(str(value)) + 2) * 256
            if (worksheet.col(col).width < width):
                worksheet.col(col).width = width
    workbook.save(file_name)