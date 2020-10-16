import random
import sys
import openpyxl
import win32com.client as win32

def convert(stri):
    stri = list(stri)
    str_output = []
    for el in stri:

        if el.isdecimal():

            str_output.append(el)
        elif el.isalpha():
            str_output.append(el.lower())
    str_output = ''.join(str_output)
    n = 2
    str_output = [str_output[i:i + n] for i in range(0, len(str_output), n)]
    str_output = (':'.join(str_output))
    return str_output



def fill_cells_by_small_list(start_row, start_col, filename, lst):
    start_col = col_index(start_col.upper())
    wb = oxl.load_workbook(filename)
    sheet = wb.active
    for col in range(0, len(lst)):
        sheet.cell(row=start_row, column=start_col + col).value = lst[col]
    wb.save(filename)
def read_file()