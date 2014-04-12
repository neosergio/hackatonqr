#!/usr/bin/python
#-*- coding:utf-8 -*-

#import modules
import csv
import os
import io

#files to import and temporaly generate sql file
CSV_FILE = 'participants.csv'

#open CSV file
print "==== Read CSV file ===="
import_file = csv.reader(open(CSV_FILE))

#create and open a temporally file to store sql queries
print "==== Create a temporally file to store insertion queries ===="
os.system('touch tmp_import.sql')
import_sql_file = open('tmp_import.sql', 'a')

#pass CSV to tmp_import.sql
counter = 0
for row in import_file:
    counter += 1
    query = 'insert into proyectos_participante values (null,null,"%s %s","%s");\n' % (row[0], row[1], row[2])
    print "== Record %i ==" % (counter)
    import_sql_file.write(query)
 
#close the temporally file  
import_sql_file.close()

#execute the command to import
print "==== Import insertion queries to the database ===="
COMMAND_TO_IMPORT = "sqlite3 db.sqlite3 < tmp_import.sql"
os.system(COMMAND_TO_IMPORT)

print "==== Delete the temporally file ===="
#delete temporally file
os.system('rm tmp_import.sql')

