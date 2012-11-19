# -*- coding: utf-8 -*-

import sqlite3 as lite
from xlrd import open_workbook
import unicodedata



book = open_workbook('Inscritos_2010-2011.xls','cp1252')
sheet = book.sheet_by_index(30)
con = lite.connect('test.db')
query = con.cursor()
query.execute("create table if not exists inscricoes(row char(50))")

for x in range(2, sheet.nrows - 1):
    for y in range(0, sheet.nrows - 1):
        word = unicodedata.normalize('NFKD', unicode(sheet.cell_value(x,y))).encode('ascii','ignore')
        if word == '' and x == 2:
            word = unicodedata.normalize('NFKD', unicode(sheet.cell_value(x,y))).encode('ascii','ignore') + '_' +str(y)
            pass
        elif word == '' and x > 2:
            word = unicodedata.normalize('NFKD', unicode(sheet.cell_value(x - 1,y))).encode('ascii','ignore')
            pass
        if (48 > ord(word[0]) or 57 < ord(word[0])) and x == 2:
            query.execute('ALTER TABLE inscricoes ADD {0} CHAR(100)'.format((word.replace(' ','_')).replace(':','')))
            pass
        elif x !=2:
            query.execute('insert into inscricoes({0}) values({1})'.format(unicodedata.normalize('NFKD', unicode(sheet.cell_value(x,2))).encode('ascii','ignore'),word.replace(':','')))
            pass
        elif 48 < ord(word[0])<57 and x == 2:
            query.execute('ALTER TABLE inscricoes ADD ano_{0} CHAR(100)'.format(((word.replace(' ','_')).replace(':','')).replace('/','_')))
            pass
        pass
    pass
