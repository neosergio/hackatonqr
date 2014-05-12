#!/usr/bin/python
#-*- coding:utf-8 -*-

#import modules
import os
import sys
import xlrd

#file to import through parameter
#i.e python import-projects-data.py participants.xlsx
try:
    EXCEL_FILE = sys.argv[1]
except:
    print "An argument is required"
    print "Usage: python import-projects-data.py projects.xlsx"
    sys.exit()

#open Excel file
print "==== Open Excel file ===="
import_file = xlrd.open_workbook(EXCEL_FILE)
sheet = import_file.sheet_by_index(0)

#create and open a temporally file to store sql queries
print "==== Create a temporally file to store insertion queries ===="

#generate temporaly generate sql file
os.system('touch tmp_import.sql')
import_sql_file = open('tmp_import.sql', 'a')

#pass CSV to tmp_import.sql
counter = 0
for row in range(1, sheet.nrows):
    counter += 1
    print "== Record %i ==" % (counter)
    if (EXCEL_FILE == "staff.xlsx"):
        # The excel file must have these fields, with headers:
        # name, email
        name = sheet.cell(row,0).value
        email = sheet.cell(row,1).value
        query = 'insert into proyectos_participante values (null,null,"%s","%s");\n' % (name, email)
    else:
        # The Excel file must have these fields, with headers:
        # lastname, name, email
        lastname = sheet.cell(row, 0).value
        name = sheet.cell(row, 1).value
        email = sheet.cell(row, 2).value
        #building the query
        previous_query = 'insert into proyectos_participante values (null,null,"%s %s","%s");\n'
        values = (name, lastname, email)
        query = (previous_query) % values

    #write the import file, row by row
    import_sql_file.write(query.encode("UTF-8"))
 
#close the temporally file  
import_sql_file.close()

#execute the command to import
print "==== Import insertion queries to the database ===="
COMMAND_TO_IMPORT = "sqlite3 db.sqlite3 < tmp_import.sql"
os.system(COMMAND_TO_IMPORT)

print "==== Delete the temporally file ===="
#delete temporally file
os.system('rm tmp_import.sql')

