# IT23666610 – ITPM Assignment 01
### BSc (Hons) in Information Technology | Year 3 | Semester 1
**Unit:** IT3040 – IT Project Management (ITPM)

---

## 📌 Assignment Overview

**Option 1: Transliteration Accuracy Testing** *(for students familiar with Sinhala)*

This assignment evaluates the accuracy of the **Chat Sinhala transliteration** feature available at:
🔗 [https://www.pixelssuite.com/chat-translator](https://www.pixelssuite.com/chat-translator)

The objective is to assess how accurately the application converts **chat-style Singlish input into Sinhala output**, by identifying 50 test cases where the system fails and automating them using **Playwright**.

---

## 🎯 Objectives

- Identify **50 negative test cases** where the system fails to correctly convert chat-style Singlish into Sinhala
- Cover at least **2 test cases for each of the 24 Singlish input types** (see Appendix 1 of the assignment)
- Automate all scenarios using **Playwright**
- Record execution results in the provided Excel file (`Assignment 1 - Test cases.xlsx`)

---

## 📁 Repository Structure

```
IT23666610-ITPM_Assignment_01/
│
├── test_automation/                  # Playwright project folder
│   ├── test_automation.py            # Main Playwright automation script
│   ├── Assignment 1 - Test cases.xlsx  # Excel file with test cases & results
│   └── (other config/dependency files)
│
├── Assignment 1 - Option 1 - For students familiar with Sinhala.pdf  # Assignment document
├── Automation Steps - Option 1.pdf   # Step-by-step automation guide
└── README.md                         # This file
```

---

## ⚙️ Prerequisites

Before running the tests, make sure the following are installed:

- **Python 3.11 / 3.12**
- **Google Chrome** (recommended) or let Playwright install Chromium automatically
- **pip** (Python package manager)

---

## 🚀 Setup & Installation

### Step 1 – Extract the project

Save and extract the ZIP file to your `D:` drive:
```
D:\test_automation
```

### Step 2 – Open Command Prompt and navigate to the folder

```bash
cd /d D:\test_automation
```

### Step 3 – Install dependencies *(one-time setup)*

```bash
pip install -U pip
pip install playwright openpyxl
playwright install
```

---

## ▶️ Running the Tests

From the `D:\test_automation` directory, run the following command:

```bash
python test_automation.py --excel "test_automation/Assignment 1 - Test cases.xlsx" --url "https://www.pixelssuite.com/chat-translator" --wait-ms 5000 --type-delay-ms 80 --slow-mo-ms 200 --save-every 1 --keep-open
```

---

## 📊 Checking Results

After the script finishes:

1. Go to the `test_automation/` folder
2. Open `Assignment 1 - Test cases.xlsx`
3. Verify the **Actual output** and **Status** columns — these are auto-filled by the script
4. Manually fill in the two additional columns:
   - **Singlish input types covered**
   - **Evidence or rationale for the input type covered**

---

## 📋 Test Case Format

| Column | Description |
|--------|-------------|
| TC ID | Starts with `Neg_` for negative test cases (e.g., `Neg_0001`) |
| Input length type | `S` (≤30 chars), `M` (31–299 chars), `L` (300–450 chars) |
| Input | The Singlish text to test |
| Expected output | The correct Sinhala translation |
| Actual output | Auto-filled by Playwright script |
| Status | Auto-filled: `Pass` or `Fail` |
| Singlish input types covered | Manually filled (e.g., Question forms, Greetings) |
| Evidence or rationale | Manually filled explanation |

---

## 🗂️ 24 Singlish Input Types Covered

1. Question forms
2. Command forms
3. Greetings
4. Requests
5. Responses
6. Repeated Words
7. Inputs with Punctuation Marks
8. Romanization / Spelling Variants
9. Isolated English Word Insertions in Singlish
10. Multi-Word English Phrases in Singlish
11. English Digital Terms in Singlish
12. Platform/App Names in Singlish
13. English Abbreviations/Acronyms in Singlish
14. English Clipped Forms in Singlish
15. Place Names Embedded in Singlish
16. Person Names Embedded in Singlish
17. Inputs with Numbers and Numeric Suffixes
18. Inputs with Currency
19. Inputs with Time Formats
20. Inputs with Dates
21. Inputs with Unit of Measurements
22. Inputs with Slang and Casual Phrasing
23. Online Identifiers in Singlish
24. Inputs Containing Emojis

---

## ⚠️ Important Notes

- All **50 test cases must be negative** (TC IDs begin with `Neg_`)
- Do **NOT** include any examples from Appendix 1 or Appendix 2 of the assignment
- The Excel file will be checked for **plagiarism** — similarity score must be ≤ 10%
- Ensure this **GitHub repository is publicly accessible** for marking

---

## 📬 Submission

- Rename all files with your **registration number**: `IT23666610`
- Create a folder named `IT23666610` and paste all required files
- Zip the folder and upload to **CourseWeb** → `Assignment 1 Answer: Option 1`
- **Deadline:** 5th May

---

*Student Registration Number: IT23666610*