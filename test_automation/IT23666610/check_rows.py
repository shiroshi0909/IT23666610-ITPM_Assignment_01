import sys, io, openpyxl
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
wb = openpyxl.load_workbook('IT23666610_Assignment 1 - Test cases.xlsx')
ws = wb.active
for r in [2, 23, 26, 32, 33]:
    tc = ws.cell(row=r, column=1).value
    inp = ws.cell(row=r, column=3).value
    actual = ws.cell(row=r, column=5).value
    status = ws.cell(row=r, column=6).value
    print(f'Row {r}: TC={tc} | Status={status} | Actual="{actual}" | Input="{inp}"')
