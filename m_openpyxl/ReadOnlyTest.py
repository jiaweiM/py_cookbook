from openpyxl import load_workbook

wb = load_workbook(filename="Z:\MaoJiawei\dataset-2\result\open_0.01_v7.1\pFind_raw.xlsx", read_only=True)
ws = wb['big_data']

for row in ws.rows:
    for cell in row:
        print(cell.value)
