import sys, io, openpyxl
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

wb = openpyxl.load_workbook('IT23666610_Assignment 1 - Test cases.xlsx')
ws = wb.active

# Fix rows 35, 36, 37:
# - Actual output = "Failed to fetch (Server API error)" (what the site showed)
# - Status = FAIL (translator failed — either wrong output or server error = failure)
# - Fix length types based on actual char counts

fixes = [
    {
        "row": 35,
        "tc_id": "Neg_0034",
        "input": "mama 1st time Sri Lanka giya wediya",
        "expected": "මම 1st time Sri Lanka ගිය වෙදිය",
        "actual": "Failed to fetch (API error)",
        "status": "FAIL",
        "cat": "Inputs with Numbers and Numeric Suffixes",
        "rationale": "Rationale: Input includes number with suffix '1st'"
    },
    {
        "row": 36,
        "tc_id": "Neg_0035",
        "input": "USD 150 dennek gather wuna",
        "expected": "USD 150 දෙනෙක් gather වුනා",
        "actual": "Failed to fetch (API error)",
        "status": "FAIL",
        "cat": "Inputs with Currency",
        "rationale": "Rationale: Input includes currency 'USD'"
    },
    {
        "row": 37,
        "tc_id": "Neg_0036",
        "input": "me jacket eka GBP 80k withara",
        "expected": "මේ jacket එක GBP 80ක් විතර",
        "actual": "Failed to fetch (API error)",
        "status": "FAIL",
        "cat": "Inputs with Currency",
        "rationale": "Rationale: Input includes currency 'GBP'"
    },
]

for fix in fixes:
    r = fix['row']
    inp = fix['input']
    char_count = len(inp)
    if char_count <= 30:
        lt = 'S'
    elif char_count <= 299:
        lt = 'M'
    else:
        lt = 'L'
    
    ws.cell(row=r, column=1).value = fix['tc_id']
    ws.cell(row=r, column=2).value = lt
    ws.cell(row=r, column=3).value = fix['input']
    ws.cell(row=r, column=4).value = fix['expected']
    ws.cell(row=r, column=5).value = fix['actual']
    ws.cell(row=r, column=6).value = fix['status']
    ws.cell(row=r, column=7).value = fix['cat']
    ws.cell(row=r, column=8).value = fix['rationale']
    print(f"Row {r}: {inp} ({char_count} chars) -> LenType={lt}, Status={fix['status']}")

wb.save('IT23666610_Assignment 1 - Test cases.xlsx')
print("\nSaved.")

# Final count
wb2 = openpyxl.load_workbook('IT23666610_Assignment 1 - Test cases.xlsx')
ws2 = wb2.active
counts = {}
for row in range(2, ws2.max_row+1):
    s = str(ws2.cell(row=row, column=6).value or '')
    counts[s] = counts.get(s, 0) + 1
print("Final Status Summary:")
for k, v in counts.items():
    print(f"  {k}: {v}")
