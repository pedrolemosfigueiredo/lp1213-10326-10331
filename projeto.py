# -*- coding: utf-8 -*-

import csv
import sqlite3 as lite
from Tkinter import *
from xlrd import open_workbook
import unicodedata
import sqlalchemy
import unicodedata


ORDEM = 0
DADOS1 = 1
DADOS2 = 2

book = open_workbook('Inscritos_2010-2011.xls','cp1252')
sheet = book.sheet_by_index(30)
con = lite.connect('test.db')

query = con.cursor()
query.execute("CREATE TABLE IF NOT EXISTS inscricoes(row char(50))")

print unicodedata.normalize('NFKD', unicode(sheet.cell_value(0,0))).encode('ascii','ignore')






# unicodedata.normalize('NFKD', unicode(sheet.cell_value(5,0))).encode('ascii','ignore')
'''
def get_not_empty(row_position, sheet)
    if sheet.cell_value
'''






for x in range(2, sheet.nrows - 1):
    for y in range (1, sheet.ncols - 1):
   # query.execute('alter table inscricoes(add' + str(sheet.cell(x, 0))  + ')')
##        print unicode(sheet.cell_value(x, y)), x, y 
        print 'ALTER TABLE inscricoes ADD {0} CHAR(100)'.format(unicodedata.normalize('NFKD', unicode(sheet.cell_value(x,y))).encode('ascii','ignore').replace(':',''))
        query.execute('ALTER TABLE inscricoes ADD {0} CHAR(100)'.format(unicodedata.normalize('NFKD', unicode(sheet.cell_value(x,y))).encode('ascii','ignore').replace(':','')))
        pass
    pass


'''for x in range(sheet.ncols):
    for y in range(2, sheet.nrows):
        print sheet.cell(x, y)
        query.execute("alter table inscricoes(add" + sheet.cell(x, +
                      ")")
        pass
    
    pass'''

        

