import fitz
import sys

def read_pdf(file_path, out_path):
    doc = fitz.open(file_path)
    with open(out_path, 'w', encoding='utf-8') as f:
        for page in doc:
            f.write(page.get_text())

read_pdf("Automation Steps - Option 1.pdf", "out1.txt")
read_pdf("Assignment 1 - Option 1 - For students familiar with Sinhala.pdf", "out2.txt")
