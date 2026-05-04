"""
Re-runs Playwright ONLY for the rows where Actual output is None/empty.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from playwright.sync_api import sync_playwright
import time, re, openpyxl

TARGET_ROWS = [26, 32, 33]  # Rows 2, 23 already done
EXCEL_PATH = "IT23666610_Assignment 1 - Test cases.xlsx"
URL = "https://www.pixelssuite.com/chat-translator"

def dismiss_overlays(page):
    for name_pat in [r"^(Accept|I Agree|Agree|OK|Got it)$", r"^(Accept all|Accept All)$"]:
        try:
            btn = page.get_by_role("button", name=re.compile(name_pat, re.IGNORECASE)).first
            if btn.is_visible():
                btn.click(timeout=2000)
                page.wait_for_timeout(500)
        except Exception:
            pass

wb = openpyxl.load_workbook(EXCEL_PATH)
ws = wb.active

tasks = []
for r in TARGET_ROWS:
    inp = ws.cell(row=r, column=3).value or ''
    exp = ws.cell(row=r, column=4).value or ''
    tasks.append((r, str(inp).strip(), str(exp).strip()))

print("Will re-test these rows:")
for r, inp, exp in tasks:
    print(f"  Row {r}: {inp}")
print()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=200)
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
        print(f"\nTesting Row {row_idx}: {singlish}")
        dismiss_overlays(page)

        prev = ""
        try:
            prev = output_loc.input_value() or ""
        except Exception:
            pass

        try:
            input_loc.click(timeout=3000)
            page.keyboard.press("Control+A")
            page.keyboard.press("Backspace")
            input_loc.type(singlish, delay=80)
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

        page.wait_for_timeout(7000)

        actual = ""
        for _ in range(8):
            try:
                cur = output_loc.input_value() or ""
                if cur and cur != prev:
                    actual = cur
                    break
            except Exception:
                pass
            page.wait_for_timeout(1000)

        if not actual:
            actual = "N/A (UI Error)"

        status = "PASS" if actual == expected else "FAIL"
        ws.cell(row=row_idx, column=5).value = actual
        ws.cell(row=row_idx, column=6).value = status
        print(f"  Status: {status}")
        wb.save(EXCEL_PATH)

    browser.close()

print("\nDone. Saved to", EXCEL_PATH)

# Final check
wb2 = openpyxl.load_workbook(EXCEL_PATH)
ws2 = wb2.active
empty = [r for r in range(2, ws2.max_row+1) if ws2.cell(row=r, column=5).value is None]
print(f"Remaining None rows: {empty}")
