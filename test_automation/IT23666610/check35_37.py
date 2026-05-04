import sys, io, openpyxl
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

wb = openpyxl.load_workbook('IT23666610_Assignment 1 - Test cases.xlsx')
ws = wb.active

# Check rows 35, 36, 37 current state
print("Current state of rows 35, 36, 37:")
for r in [35, 36, 37]:
    tc = ws.cell(row=r, column=1).value
    lt = ws.cell(row=r, column=2).value
    inp = ws.cell(row=r, column=3).value
    exp = ws.cell(row=r, column=4).value
    actual = ws.cell(row=r, column=5).value
    status = ws.cell(row=r, column=6).value
    cat = ws.cell(row=r, column=7).value
    print(f"\nRow {r}:")
    print(f"  TC ID   : {tc}")
    print(f"  Len     : {lt}")
    print(f"  Input   : {inp}")
    print(f"  Expected: {exp}")
    print(f"  Actual  : {actual}")
    print(f"  Status  : {status}")
    print(f"  Category: {cat}")
