#!/usr/bin/env python
# -*- coding: utf-8  -*-

import json, ttk, Tix, re, sqlCustom, fileCustom
from Tkinter import *
from ScrolledText import ScrolledText
from Tkconstants import *

window = Tix.Tk()

sql = sqlCustom.MySQL(user = 'root', host = "localhost", passwd = "secret", db = "bike_test")
sql.ConnectDatabase()


class go_dump:
    pass

#print window.tix_configure()
print('calculate count of strings')
workFile = fileCustom.File('bike_dump.sql')
workFile.get_count_lines()

print 'file has ', workFile.lines_count, ' strings'

pattern = '^INSERT'

pattern_obj = re.compile(pattern)

for line_num in range(workFile.lines_count):
    string = workFile.get_next_line()
    res = pattern_obj.match(string)
    if res:
        print(workFile.curr_line - 1)
        print string
        print 'result of request', sql.execute(string)

print('end of script')