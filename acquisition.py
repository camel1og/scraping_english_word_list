import ssWrite

workbooks = ssWrite.accessSpleadSheet()
print(workbooks.worksheet('中学一年生単語一覧').cell(1,1).value)
