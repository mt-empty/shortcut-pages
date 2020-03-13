# Xlrd

> Source: https://github.com/python-excel/tutorial/raw/master/python-excel.pdf

> Aliases: python-xls-files

$ Workbooks
    `book=open_workbook(contents=mmap(f.fileno(),0,access=ACCESS_READ))
>                                  {{Opnen workbook from mmap}} 
    `book=open_workbook(file_contents=aString)
>                                  {{Open workbook from file content as string}} 
    `book=open_workbook(filename)  {{Open workbook from file}} 

$ Sheets
    `sheets=book.sheets()          {{Get the list of sheets}} 
    `nSheets=book.nsheets          {{Get the number of sheets in the book}} 
    `names=book.sheet_names()      {{Get the list of sheet names}} 
    `sheet=book.sheet_by_index(i)  {{Get sheet #i in the book}} 
