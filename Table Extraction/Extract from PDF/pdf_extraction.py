"""
We will use camelot (pip install camelot-py) to extract tables found in a PDF file
into another format, for example csv format. In this directory, we have an example pdf file with a table located inside of it

ghostscript is also required to have installed, as camelot is dependent on it.
camelot docs: https://camelot-py.readthedocs.io/en/master/
full camelot docs: https://app.readthedocs.org/projects/camelot-py/downloads/pdf/master/
"""

import camelot

tables = camelot.read_pdf('./example.pdf')                     #camelot.read_pdf will only read the first page of a PDF document by default. You can specify which page it reads e.g. pages='2,3' will read the second and third pages and pages='all' will read all pages
                                                               #the 'tables' variable is now a TableList object, which holds a list of the tables found in the PDF file.

print(tables)                                                  #this will print: "<TableList n=1>" which means that in the PDF file, one table was found.

tables.export('./table_data.csv', f='csv', compress=True)      #this exports our list of tables in the 'table' variable into a zip file which contains all the tables exported into a csv format. f=csv means the format is csv, and we compress the output files into a .zip.
                                                               #the .export() function is apart of camelot library

                                                               #in this case, since our PDF file only has 1 table included, the .export() function will take that one table, export it as a csv file called 'table_data.csv' and zip it. If there were multiple tables in our 
                                                               #PDF file, it would automatically name the files such as 'table_data-1.csv, table_data-2.csv' etc and place them all in the zip file.

#tables[0].to_csv('./table_data.csv')                           #alternatively, if we only wanted to work with a single table at a time, we can just use this method.

