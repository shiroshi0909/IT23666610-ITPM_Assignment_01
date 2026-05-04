# Assignment 1 – Transliteration Accuracy Testing
**IT3040 – IT Project Management | BSc (Hons) in Information Technology – Year 3, Semester 1**

**Student Registration Number:** IT23666610

---

## Overview

This project automates the testing of the **Chat Sinhala transliteration function** at [https://www.pixelssuite.com/chat-translator](https://www.pixelssuite.com/chat-translator) using **Playwright** and **Python**.

The automation evaluates how accurately the application converts chat-style Singlish input into Sinhala output, recording the actual output and pass/fail status for 50 negative test cases spanning all 24 Singlish input types defined in Appendix 1 of the assignment.

---

## Project Structure

```
IT23666610/
├── test_automation.py              # Main Playwright automation script
├── IT23666610_Assignment 1 - Test cases.xlsx  # Test case data with results
├── IT23666610_Git_Link.txt         # GitHub repository link
└── README.md                       # This file
```

---

## Prerequisites

- Python 3.11 or 3.12
- Google Chrome (recommended) or Playwright's bundled Chromium

---

## Installation

### Step 1 – Install Python dependencies
```bash
pip install -U pip
pip install playwright openpyxl
```

### Step 2 – Install Playwright browsers
```bash
playwright install
```

---

## Running the Tests

Run the following command from the project directory:

```bash
python test_automation.py --excel "IT23666610_Assignment 1 - Test cases.xlsx" --url "https://www.pixelssuite.com/chat-translator" --wait-ms 5000 --type-delay-ms 80 --slow-mo-ms 200 --save-every 1 --keep-open
```

### Command-Line Arguments

| Argument | Description | Default |
|---|---|---|
| `--excel` | Path to the Excel test case file | Auto-detected |
| `--url` | URL of the translator application | `https://www.pixelssuite.com/chat-translator` |
| `--wait-ms` | Time (ms) to wait for translation output after each input | `5000` |
| `--type-delay-ms` | Delay (ms) between keystrokes when typing inputs | `80` |
| `--slow-mo-ms` | Slow-motion delay (ms) for browser interactions | `200` |
| `--save-every` | Save the Excel file after every N test cases | `1` |
| `--headless` | Run browser in headless mode (no visible window) | `False` |
| `--keep-open` | Keep the browser open after all tests complete | `False` |

---

## How It Works

1. The script reads the test inputs from the Excel file (`Input` column).
2. It opens the Pixelssuite Chat Translator in a Chromium browser.
3. For each row, it types the Singlish input, waits for the translation, and captures the Sinhala output.
4. It compares the actual output to the expected output and records `PASS` or `FAIL` in the `Status` column.
5. All results are saved back to the Excel file automatically.

---

## Test Case Summary

| Status | Count |
|--------|-------|
| FAIL | 39 |
| PASS | 3 |
| UI Error | 8 |

All 50 test cases are **negative test cases** (designed to identify failures in the transliteration system). They cover all **24 Singlish input types** as specified in Appendix 1 of the assignment.
