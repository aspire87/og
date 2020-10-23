import random
import sys
import openpyxl
import win32com.client as win32

import pickle
import os


class Statement:
    '''Saving python data(dicts,lists) in binary to use in future
    Need to create class object(filename can contains file path like '/usr/example/example.bin') .
    Then create new dump
    One file can contains only one object
    You can only rewrite, or read dump, be carefull
    Method 'read' returns saved objects
    Method 'rewrite' clears the dump file and write new object into it '''

    def __init__(self, filename):
        self.filepath = filename  # Path to binary

    def _checkfile(self):
        filename = self.filepath
        if os.path.exists(filename):
            return True
        return False

    def newdump(self):
        if not self._checkfile():
            with open(self.filepath, 'wb') as fl:
                pass
        else:
            print('File already exists, use method rewrite')

    def rewrite(self,data):
        if self._checkfile():
            with open(self.filepath, 'wb') as fl:
                pickle.dump(data, fl)
        else:
            print('File does not exists, use method newdump')

    def read(self):
        if self._checkfile():
            with open(self.filepath, 'rb') as fl:
                data = pickle.load(fl)
            return data
        else:
            print('File does not exists, use method newdump')


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
