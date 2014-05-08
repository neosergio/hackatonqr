#!/usr/bin/python
#-*- coding:utf-8 -*-

#import modules
import xlrd
import os

#files to import and temporaly generate sql file
EXCEL_FILE = 'projects.xlsx'

#open Excel file
print "==== Open Excel file ===="
import_file = xlrd.open_workbook(EXCEL_FILE)
sheet = import_file.sheet_by_index(0)

#create and open a temporally file to store sql queries
print "==== Create a temporally file to store insertion queries ===="
os.system('touch tmp_import.sql')
import_sql_file = open('tmp_import.sql', 'a')

#pass CSV to tmp_import.sql
counter = 0
for row in range(1, sheet.nrows):
    counter += 1
    print "== Record %i ==" % (counter)
    # The Excel file must have these fields, with headers:
    # name, description, owner_name, technology(optional), category(optional), email(optional)
    # #max_participants(integer), status, url(optional)
    name = sheet.cell(row,0).value
    description = sheet.cell(row,1).value
    owner_name = sheet.cell(row,2).value
    technology = sheet.cell(row,3).value
    email = sheet.cell(row,5).value
    max_participants = sheet.cell(row,6).value
    status = sheet.cell(row,7).value
    url = sheet.cell(row,8).value
    
    query = 'insert into proyectos_proyecto values (null,"%s","%s","%s","%s","%s",%s);\n'
    values = (name, description, owner_name, technology, email,max_participants)
    
    numero = int(round(max_participants))
    print query % values
    #import_sql_file.write(query)
#close the temporally file  
#import_sql_file.close()

#execute the command to import
print "==== Import insertion queries to the database ===="
#COMMAND_TO_IMPORT = "sqlite3 db.sqlite3 < tmp_import.sql"
#os.system(COMMAND_TO_IMPORT)

print "==== Delete the temporally file ===="
#delete temporally file
#os.system('rm tmp_import.sql')
