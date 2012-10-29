# -*- coding: utf-8 -*-

import csv
import sqlite3 as lite
from Tkinter import *
from xlrd import open_workbook
import unicodedata



ORDEM = 0
DADOS1 = 1
DADOS2 = 2

'''app = Tk()
app.tittle = ("fuck that shit")'''

book = open_workbook('Inscritos_2010-2011.xls','cp1252')

sheet = book.sheet_by_index(30)

print sheet.name



con = lite.connect('test.db')

query = con.cursor()

query.execute("CREATE TABLE IF NOT EXISTS inscricoes(row char(50))")

for x in range(sheet.ncols):
    query.execute('alter table inscricoes(add' + str(sheet.cell(x, 0))  + ')')
    pass

'''for x in range(sheet.ncols):
    for y in range(2, sheet.nrows):
        print sheet.cell(x, y)
        query.execute("alter table inscricoes(add" + sheet.cell(x, +
                      ")")
        pass
    
    pass'''

        

