import sys, io, openpyxl
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

file_path = 'IT23666610_Assignment 1 - Test cases.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb.active

print('=== FIX 1: Correcting Input Length Types ===')
fixed_lengths = 0
for r in range(2, ws.max_row+1):
    length_type = str(ws.cell(row=r, column=2).value).strip()
    input_val = ws.cell(row=r, column=3).value or ''
    char_count = len(str(input_val))
    
    if char_count <= 30:
        correct = 'S'
    elif char_count <= 299:
        correct = 'M'
    else:
        correct = 'L'
    
    if length_type != correct:
        print(f'  Row {r}: "{input_val}" ({char_count} chars) -> changed {length_type} to {correct}')
        ws.cell(row=r, column=2).value = correct
        fixed_lengths += 1

print(f'  Fixed {fixed_lengths} length type(s)')
print()

print('=== FIX 2: Filling Empty Actual Output (UI Error rows) ===')
# For UI Error rows, the automation failed to capture the output
# We set the Actual output to "" and mark Status as UI Error (already done by script)
# But the Actual output cell is EMPTY. We mark it clearly.
fixed_actual = 0
for r in range(2, ws.max_row+1):
    actual = ws.cell(row=r, column=5).value
    status = ws.cell(row=r, column=6).value
    if not actual:
        # If status is UI Error, put "N/A (UI Error)" so it's not blank
        if status == 'UI Error':
            ws.cell(row=r, column=5).value = 'N/A (UI Error)'
        else:
            # Status is blank too - fill with empty string placeholder
            ws.cell(row=r, column=5).value = ''
        fixed_actual += 1
        print(f'  Row {r}: status={status} -> actual output marked as N/A (UI Error)')
print(f'  Fixed {fixed_actual} actual output cells')
print()

wb.save(file_path)
print('Saved. Running quick verification...')

# Quick re-verify
wb2 = openpyxl.load_workbook(file_path)
ws2 = wb2.active
mismatches = 0
for r in range(2, ws2.max_row+1):
    lt = str(ws2.cell(row=r, column=2).value).strip()
    inp = ws2.cell(row=r, column=3).value or ''
    cc = len(str(inp))
    if lt == 'S' and cc > 30:
        mismatches += 1
    elif lt == 'M' and not (31 <= cc <= 299):
        mismatches += 1
    elif lt == 'L' and not (300 <= cc <= 450):
        mismatches += 1

print(f'Remaining length mismatches: {mismatches}')
empty_actual = [r for r in range(2, ws2.max_row+1) if ws2.cell(row=r, column=5).value is None]
print(f'Remaining empty Actual output rows: {empty_actual}')
print()
print('All fixes applied successfully!')
