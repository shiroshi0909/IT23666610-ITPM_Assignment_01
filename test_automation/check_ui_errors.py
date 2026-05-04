import sys, io, openpyxl
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

wb = openpyxl.load_workbook('IT23666610_Assignment 1 - Test cases.xlsx')
ws = wb.active

print("=== UI Error / N/A rows ===")
for r in range(2, ws.max_row+1):
    status = str(ws.cell(row=r, column=6).value or '')
    actual = str(ws.cell(row=r, column=5).value or '')
    inp = str(ws.cell(row=r, column=3).value or '')
    tc = str(ws.cell(row=r, column=1).value or '')
    if 'UI Error' in status or 'N/A' in actual or 'UI Error' in actual:
        print(f"  Row {r} | {tc} | Status='{status}' | Actual='{actual}' | Input='{inp}'")
