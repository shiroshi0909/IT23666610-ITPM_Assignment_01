import sys, io, openpyxl
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

file_path = 'IT23666610_Assignment 1 - Test cases.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb.active

print('=== FULL AUDIT OF EXCEL FILE ===')
print(f'Sheet: {ws.title}')
print(f'Total data rows: {ws.max_row - 1}')
print(f'Total columns: {ws.max_column}')
print()

# Check all headers
headers = [ws.cell(row=1, column=c).value for c in range(1, ws.max_column+1)]
print('Headers:', headers)
print()

required = [
    'TC ID', 'Input length type', 'Input', 'Expected output',
    'Actual output', 'Status',
    'Singlish input types covered',
    'Evidence or rationale for the input type covered'
]
print('=== Header Check ===')
for h in required:
    found = h in headers
    status = 'OK' if found else 'MISSING'
    print(f'  [{status}] {h}')
print()

# Check TC IDs are Neg_ prefix
print('=== TC ID Prefix Check ===')
bad_ids = []
for r in range(2, ws.max_row+1):
    tc_id = ws.cell(row=r, column=1).value
    if tc_id and not str(tc_id).startswith('Neg'):
        bad_ids.append((r, tc_id))
if bad_ids:
    print('  BAD IDs:', bad_ids)
else:
    print('  [OK] All 50 TC IDs start with Neg_')
print()

# Check all 24 categories covered with at least 2 each
print('=== Singlish Input Types Coverage (must have >= 2 per category) ===')
required_cats = [
    'Question forms', 'Command forms', 'Greetings', 'Requests', 'Responses',
    'Repeated Words', 'Inputs with Punctuation Marks', 'Romanization / Spelling Variants',
    'Isolated English Word Insertions in Singlish', 'Multi-Word English Phrases in Singlish',
    'English Digital Terms in Singlish', 'Platform/App Names in Singlish',
    'English Abbreviations/Acronyms in Singlish', 'English Clipped Forms in Singlish',
    'Place Names Embedded in Singlish', 'Person Names Embedded in Singlish',
    'Inputs with Numbers and Numeric Suffixes', 'Inputs with Currency',
    'Inputs with Time Formats', 'Inputs with Dates', 'Inputs with Unit of Measurements',
    'Inputs with Slang and Casual Phrasing', 'Online Indentifiers in Singlish',
    'Inputs Containing Emojis'
]
cat_counts = {}
for r in range(2, ws.max_row+1):
    cat = ws.cell(row=r, column=7).value
    if cat:
        cat_counts[str(cat)] = cat_counts.get(str(cat), 0) + 1

all_ok = True
for cat in required_cats:
    count = cat_counts.get(cat, 0)
    ok = count >= 2
    if not ok:
        all_ok = False
    tag = 'OK' if ok else 'FAIL'
    print(f'  [{tag}] {cat}: {count}')
print()
if all_ok:
    print('  All 24 categories have at least 2 test cases!')
else:
    print('  WARNING: Some categories are missing coverage!')
print()

# Check input length types are valid
print('=== Input Length Type Check (must be S / M / L) ===')
valid_lengths = {'S', 'M', 'L'}
bad_lengths = []
for r in range(2, ws.max_row+1):
    length = ws.cell(row=r, column=2).value
    if str(length) not in valid_lengths:
        bad_lengths.append((r, length))
if bad_lengths:
    print('  BAD length types:', bad_lengths)
else:
    print('  [OK] All 50 rows have valid length type (S/M/L)')
print()

# Check for empty Actual output
print('=== Empty Cell Check ===')
empty_actual = [r for r in range(2, ws.max_row+1) if not ws.cell(row=r, column=5).value]
empty_status = [r for r in range(2, ws.max_row+1) if not ws.cell(row=r, column=6).value]
empty_cat_col = [r for r in range(2, ws.max_row+1) if not ws.cell(row=r, column=7).value]
empty_rat = [r for r in range(2, ws.max_row+1) if not ws.cell(row=r, column=8).value]
print(f'  Rows with empty Actual output: {empty_actual}')
print(f'  Rows with empty Status: {empty_status}')
print(f'  Rows with empty Singlish input types: {empty_cat_col}')
print(f'  Rows with empty Evidence/Rationale: {empty_rat}')
print()

# Chars check on Input column - S <= 30, M = 31-299, L = 300-450
print('=== Input Length vs Length Type Validation ===')
length_errors = []
for r in range(2, ws.max_row+1):
    length_type = str(ws.cell(row=r, column=2).value).strip()
    input_val = ws.cell(row=r, column=3).value or ''
    char_count = len(str(input_val))
    if length_type == 'S' and char_count > 30:
        length_errors.append(f'Row {r}: declared S but has {char_count} chars: "{input_val}"')
    elif length_type == 'M' and not (31 <= char_count <= 299):
        length_errors.append(f'Row {r}: declared M but has {char_count} chars: "{input_val}"')
    elif length_type == 'L' and not (300 <= char_count <= 450):
        length_errors.append(f'Row {r}: declared L but has {char_count} chars: "{input_val}"')
if length_errors:
    print('  LENGTH MISMATCHES:')
    for e in length_errors:
        print(f'    {e}')
else:
    print('  [OK] All input lengths match declared length type!')
print()

# Total count
print('=== Total Count ===')
count = ws.max_row - 1
tag = 'OK' if count == 50 else 'WRONG'
print(f'  [{tag}] Total test cases: {count} (required: 50)')
