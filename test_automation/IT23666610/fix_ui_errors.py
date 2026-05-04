"""
Retests all UI Error rows properly.
Strategy: 
  - Between each test, type something random to force a new translation, 
    THEN type the real input, so the output always changes.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from playwright.sync_api import sync_playwright
import re, openpyxl

UI_ERROR_ROWS = [2, 22, 23, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40]
EXCEL_PATH = "IT23666610_Assignment 1 - Test cases.xlsx"
URL = "https://www.pixelssuite.com/chat-translator"

wb = openpyxl.load_workbook(EXCEL_PATH)
ws = wb.active

tasks = []
for r in UI_ERROR_ROWS:
    inp = str(ws.cell(row=r, column=3).value or '').strip()
    exp = str(ws.cell(row=r, column=4).value or '').strip()
    tasks.append((r, inp, exp))

print(f"Retesting {len(tasks)} UI Error rows...")

def clear_and_type(page, input_loc, text, delay=80):
    input_loc.click(timeout=3000)
    page.keyboard.press("Control+A")
    page.keyboard.press("Delete")
    page.wait_for_timeout(300)
    # Verify cleared
    try:
        val = input_loc.input_value()
        if val:
            input_loc.fill("")
            page.wait_for_timeout(300)
    except Exception:
        pass
    input_loc.type(text, delay=delay)

def get_output(output_loc):
    try:
        v = output_loc.input_value()
        if v:
            return v.strip()
    except Exception:
        pass
    try:
        v = output_loc.inner_text()
        if v:
            return v.strip()
    except Exception:
        pass
    return ""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.set_default_timeout(60000)

    page.goto(URL, wait_until="domcontentloaded")
    try:
        page.wait_for_load_state("networkidle", timeout=30000)
    except Exception:
        pass
    page.wait_for_selector("textarea", timeout=30000)
    print("Page loaded.")

    input_loc = page.locator('textarea[placeholder*="English"]').first
    output_loc = page.locator('textarea[placeholder*="Sinhala"]').first
    action_btn = page.get_by_role("button", name=re.compile(r"^Transliterate$", re.IGNORECASE)).first

    for row_idx, singlish, expected in tasks:
        print(f"\nRow {row_idx}: {singlish}")

        # Step 1: Type a dummy input first to reset the state
        try:
            clear_and_type(page, input_loc, "xyzreset", delay=30)
            action_btn.click()
            page.wait_for_timeout(3000)
            dummy_out = get_output(output_loc)
        except Exception as e:
            print(f"  Dummy reset failed: {e}")
            dummy_out = ""

        # Step 2: Now type the real input
        try:
            clear_and_type(page, input_loc, singlish, delay=80)
        except Exception as e:
            print(f"  Type error: {e}")
            ws.cell(row=row_idx, column=5).value = "N/A (UI Error)"
            ws.cell(row=row_idx, column=6).value = "FAIL"
            wb.save(EXCEL_PATH)
            continue

        try:
            action_btn.click()
        except Exception:
            pass

        # Step 3: Wait for output to change from dummy
        page.wait_for_timeout(5000)

        actual = ""
        for attempt in range(12):
            cur = get_output(output_loc)
            if cur and cur != dummy_out:
                actual = cur
                break
            page.wait_for_timeout(1000)

        if not actual:
            print(f"  Still no output after retries — marking as FAIL with N/A")
            actual = "N/A (UI Error)"
            status = "FAIL"
        else:
            status = "PASS" if actual == expected else "FAIL"

        ws.cell(row=row_idx, column=5).value = actual
        ws.cell(row=row_idx, column=6).value = status
        print(f"  Status: {status}")
        wb.save(EXCEL_PATH)

    browser.close()

print("\n=== Done ===")
# Final check
wb2 = openpyxl.load_workbook(EXCEL_PATH)
ws2 = wb2.active
still_ui_error = []
for r in range(2, ws2.max_row+1):
    s = str(ws2.cell(row=r, column=6).value or '')
    a = str(ws2.cell(row=r, column=5).value or '')
    if 'UI Error' in s:
        still_ui_error.append(r)
print(f"Rows still with 'UI Error' status: {still_ui_error}")
